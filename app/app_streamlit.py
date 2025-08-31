import streamlit as st
import joblib
import numpy as np


model = joblib.load('model/regression_model.pkl')


st.set_page_config(page_title="Insurance Charges Predictor", page_icon="💰", layout="centered")
st.title("💡 Insurance Charges Prediction")
st.markdown("Predict insurance charges based on age, BMI category, and smoking status.")


st.sidebar.header("Input Details")
age = st.sidebar.slider("Age", min_value=0, max_value=100, value=30, help="Enter age in years")

smoker_input = st.sidebar.selectbox("Smoker?", ["No", "Yes"])
is_smoker = 1 if smoker_input == "Yes" else 0

bmi_input = st.sidebar.selectbox("BMI Category - Obese?", ["No", "Yes"])
bmi_obese = 1 if bmi_input == "Yes" else 0


if st.sidebar.button("Predict"):
    features = np.array([is_smoker, age, bmi_obese]).reshape(1, -1)
    prediction = model.predict(features)
    
    st.subheader("💰 Predicted Insurance Charges")
    st.success(f"${prediction[0]:,.2f}")
    st.balloons()
