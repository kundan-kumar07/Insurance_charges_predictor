import requests

url = "http://127.0.0.1:5000/predict"

# Replace values with the person you want to predict for
data = {"features": [1, 45, 0]}  # Example: smoker=1, age=45, not obese

response = requests.post(url, json=data)
print(response.json())
