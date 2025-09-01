# 💰 Insurance Charges Predictor

Cleaned and preprocessed insurance dataset (1,337 rows, 7 features): handled duplicates, encoded categorical variables (sex, smoker, region, bmi_category), and scaled numerical features.

Conducted correlation analysis & feature selection → selected top predictors (is_smoker, age, bmi_category_Obese).

Trained Linear Regression model, achieving R² = 0.80 (test) and R² = 0.73 (train).

Saved model as regression_model.pkl for integration with Streamlit app.

---

## Folder Structure

insurance_predictor/
├── data/               # Dataset(s)
├── notebook.ipynb      # Training notebook
├── model.pkl           # Trained model
└── streamlit_app.py    # Streamlit app


---

## Run Locally
1. Clone the repo:
git clone <your-repo-url>
cd insurance_predictor

2.Install dependencies:

pip install streamlit numpy pandas scikit-learn


3.Run the app:

streamlit run streamlit_app.py
