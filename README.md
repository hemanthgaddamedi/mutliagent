\# 📊 Customer Churn Prediction API



An end-to-end \*\*Machine Learning customer churn prediction system\*\* built with \*\*Python, XGBoost, Pandas, Scikit-learn, Joblib, and FastAPI\*\*.



The project predicts whether a customer is likely to churn based on customer demographics, service usage, contract information, and billing details.



The trained machine learning pipeline is exposed through a REST API using FastAPI.



\---



\## 🚀 Project Overview



Customer churn prediction helps businesses identify customers who are at risk of leaving their service.



This project accepts customer information as input and predicts:



\* Whether the customer is likely to churn

\* Churn probability

\* Classification threshold



\### Workflow



```text

Customer Data

&#x20;     ↓

FastAPI API

&#x20;     ↓

Input Validation

&#x20;     ↓

Feature Engineering

&#x20;     ↓

XGBoost Pipeline

&#x20;     ↓

Churn Probability

&#x20;     ↓

Churn Prediction

```



\---



\## ✨ Features



\* 🤖 XGBoost classification

\* ⚡ FastAPI REST API

\* 📊 Pandas-based data processing

\* 🔧 Feature engineering

\* 📈 Churn probability prediction

\* 🎯 Custom classification threshold

\* 🧩 Pydantic input validation

\* 💾 Joblib model serialization

\* 📚 Interactive Swagger documentation



\---



\## 🧠 Machine Learning



The project uses \*\*XGBoost\*\* for binary classification.



The API currently uses a classification threshold of:



```text

0.35

```



Prediction logic:



```text

Probability >= 0.35

&#x20;       ↓

&#x20;  Churn = Yes



Probability < 0.35

&#x20;       ↓

&#x20;  Churn = No

```



For example:



```text

Churn Probability = 0.68

Threshold = 0.35



0.68 >= 0.35



Prediction = Yes

```



\---



\## 🔧 Feature Engineering



The API performs feature engineering before passing the data to the trained model.



\### Tenure Group



Customers are grouped based on their tenure.



\### Service Count



The system calculates the number of services used by a customer, including:



\* Phone Service

\* Multiple Lines

\* Online Security

\* Online Backup

\* Device Protection

\* Tech Support

\* Streaming TV

\* Streaming Movies



\### Contract Indicator



The system creates an indicator for month-to-month contracts.



\---



\## 🛠️ Tech Stack



\### Programming



\* Python



\### Machine Learning



\* XGBoost

\* Scikit-learn

\* Pandas

\* NumPy



\### Backend



\* FastAPI

\* Pydantic

\* Uvicorn



\### Model Management



\* Joblib



\### Development



\* Git

\* GitHub



\---



\## 📁 Project Structure



```text

customer-churn-prediction-api/

│

├── main.py

├── requirements.txt

├── README.md

├── .gitignore

│

└── models/

&#x20;   └── churn\_xgboost\_pipeline.pkl

```



\---



\## ⚙️ Installation



\### 1. Clone the repository



```bash

git clone https://github.com/hemanthgaddamedi/mutliagent.git

cd mutliagent

```



\### 2. Create a virtual environment



Windows:



```bash

python -m venv venv

```



Activate it:



```bash

venv\\Scripts\\activate

```



\### 3. Install dependencies



```bash

pip install -r requirements.txt

```



\---



\## ▶️ Run the API



Start the FastAPI server:



```bash

uvicorn main:app --reload

```



The API will run at:



```text

http://127.0.0.1:8000

```



\---



\## 📚 API Documentation



FastAPI provides interactive API documentation.



\### Swagger UI



```text

http://127.0.0.1:8000/docs

```



\### ReDoc



```text

http://127.0.0.1:8000/redoc

```



\---



\# 🔌 API Endpoints



\## GET `/`



Checks whether the API is running.



\### Example Response



```json

{

&#x20; "message": "Customer Churn Prediction API is running"

}

```



\---



\## POST `/predict`



Predicts whether a customer is likely to churn.



\### Example Request



```json

{

&#x20; "gender": "Female",

&#x20; "SeniorCitizen": 0,

&#x20; "Partner": "Yes",

&#x20; "Dependents": "No",

&#x20; "tenure": 12,

&#x20; "PhoneService": "Yes",

&#x20; "MultipleLines": "No",

&#x20; "InternetService": "DSL",

&#x20; "OnlineSecurity": "No",

&#x20; "OnlineBackup": "Yes",

&#x20; "DeviceProtection": "No",

&#x20; "TechSupport": "No",

&#x20; "StreamingTV": "No",

&#x20; "StreamingMovies": "No",

&#x20; "Contract": "Month-to-month",

&#x20; "PaperlessBilling": "Yes",

&#x20; "PaymentMethod": "Electronic check",

&#x20; "MonthlyCharges": 55.5,

&#x20; "TotalCharges": 666.0

}

```



\### Example Response



```json

{

&#x20; "churn\_prediction": "Yes",

&#x20; "churn\_probability": 0.6812,

&#x20; "threshold": 0.35

}

```



\---



\## 📊 Input Features



| Feature            | Description                    |

| ------------------ | ------------------------------ |

| `gender`           | Customer gender                |

| `SeniorCitizen`    | Senior citizen indicator       |

| `Partner`          | Partner status                 |

| `Dependents`       | Dependent status               |

| `tenure`           | Customer tenure in months      |

| `PhoneService`     | Phone service status           |

| `MultipleLines`    | Multiple line subscription     |

| `InternetService`  | Internet service type          |

| `OnlineSecurity`   | Online security subscription   |

| `OnlineBackup`     | Online backup subscription     |

| `DeviceProtection` | Device protection subscription |

| `TechSupport`      | Technical support subscription |

| `StreamingTV`      | Streaming TV subscription      |

| `StreamingMovies`  | Streaming movies subscription  |

| `Contract`         | Contract type                  |

| `PaperlessBilling` | Paperless billing status       |

| `PaymentMethod`    | Payment method                 |

| `MonthlyCharges`   | Monthly charges                |

| `TotalCharges`     | Total charges                  |



\---



\## 🎯 Business Use Case



Customer churn prediction can help businesses identify customers who may be at risk of leaving.



Potential applications include:



\* Identifying high-risk customers

\* Customer retention campaigns

\* Personalized offers

\* Prioritizing customer support

\* Analyzing churn patterns

\* Improving customer retention



\---



\## 🔮 Future Improvements



\* \[ ] Add model evaluation metrics

\* \[ ] Add confusion matrix

\* \[ ] Add ROC-AUC evaluation

\* \[ ] Add feature importance visualization

\* \[ ] Add SHAP explainability

\* \[ ] Add Streamlit dashboard

\* \[ ] Add batch prediction

\* \[ ] Add Docker support

\* \[ ] Add automated testing

\* \[ ] Add CI/CD with GitHub Actions

\* \[ ] Deploy to cloud



\---



\## 📈 Future Explainability



SHAP can be integrated in a future version to explain individual predictions.



Example:



```text

Why is this customer predicted to churn?



↑ Month-to-month contract

↑ High monthly charges

↑ Low tenure

↑ Electronic check payment

```



This would make the prediction more interpretable for business users.



\---



\## 💡 Skills Demonstrated



This project demonstrates practical experience with:



\* Machine Learning

\* XGBoost

\* Classification

\* Feature Engineering

\* Probability-based prediction

\* Threshold tuning

\* FastAPI

\* REST APIs

\* Pandas

\* Scikit-learn

\* Pydantic

\* Joblib

\* Git/GitHub



\---



\## 👨‍💻 Author



\*\*Gaddamedi Hemanth\*\*



AI/ML Engineer | Generative AI | RAG | AI Agents | Python



Hyderabad, India



GitHub: `https://github.com/hemanthgaddamedi`



LinkedIn: `https://linkedin.com/in/hemanth-gaddamedi`



\---



\## ⭐ Project



If you find this project useful, consider giving the repository a ⭐.



