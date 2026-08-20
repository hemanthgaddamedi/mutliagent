from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
import pandas as pd
import joblib


app = FastAPI(
    title="Customer Churn Prediction API",
    version="1.0.0"
)


# --------------------------------------------------
# Load trained model
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "churn_xgboost_pipeline.pkl"

model = joblib.load(MODEL_PATH)


# --------------------------------------------------
# Input schema
# --------------------------------------------------

class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float


# --------------------------------------------------
# Home endpoint
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API is running"
    }


# --------------------------------------------------
# Prediction endpoint
# --------------------------------------------------

@app.post("/predict")
def predict_churn(customer: CustomerData):

    # Convert request to DataFrame
    data = pd.DataFrame([customer.model_dump()])

    # --------------------------------------------------
    # Feature engineering
    # --------------------------------------------------

    # Tenure group
    if data["tenure"].iloc[0] <= 12:
        data["TenureGroup"] = "0-12 months"
    elif data["tenure"].iloc[0] <= 24:
        data["TenureGroup"] = "13-24 months"
    elif data["tenure"].iloc[0] <= 48:
        data["TenureGroup"] = "25-48 months"
    else:
        data["TenureGroup"] = "49-72 months"

    # Count active services
    service_columns = [
        "PhoneService",
        "MultipleLines",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies"
    ]

    data["ServiceCount"] = sum(
        data[column].eq("Yes").astype(int)
        for column in service_columns
    )

    # Month-to-month indicator
    data["IsMonthToMonth"] = (
        data["Contract"] == "Month-to-month"
    ).astype(int)

    # --------------------------------------------------
    # Predict probability
    # --------------------------------------------------

    probability = float(model.predict_proba(data)[0][1])

    # Use the tuned threshold from your model evaluation
    threshold = 0.35

    prediction = int(probability >= threshold)

    churn_label = "Yes" if prediction == 1 else "No"

    return {
        "churn_prediction": churn_label,
        "churn_probability": round(probability, 4),
        "threshold": threshold
    }