# 💰 Insurance Charges Predictor

A web application to **predict insurance charges** based on a person's **age, BMI category (Obese or not), and smoking status**. Built with **Python, Flask, and scikit-learn**. The model is trained on sample insurance data and exposed via a REST API.

---

## **Features**

- Predict insurance charges for a person given:
  - Age
  - Smoker status (Yes/No)
  - BMI Category (Obese/Not)
- REST API backend using Flask
- Easy to integrate with a frontend (Streamlit or React)
- Cloud-deployable (Railway, Heroku, etc.)

---

## **Project Structure**

nsurance_predictor/
│
├── app_flask.py # Flask backend
├── model/
│ └── regression_model.pkl # Trained model
├── requirements.txt # Python dependencies
└── README.md

---

## Run Locally

1. Clone repo:


git clone <your-repo-url>
cd insurance_predictor



2.Install dependencies:

pip install -r requirements.txt


3.Run the app:

python app_flask.py

**Dependencies**

Python

Flask

scikit-learn==1.5.1

NumPy

pandas

cloudpickle
