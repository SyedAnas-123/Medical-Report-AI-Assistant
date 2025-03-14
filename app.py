
from flask import Flask, request, render_template
import pickle
import numpy as np

# Load the trained model from pickle file
model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract user inputs from form and convert to appropriate types
        age = int(request.form['age'])
        sex = int(request.form['sex'])  # 0 = Female, 1 = Male
        cp = int(request.form['cp'])  # Chest Pain Type (0-3)
        trestbps = int(request.form['trestbps'])  # Resting BP
        chol = int(request.form['chol'])  # Cholesterol
        fbs = int(request.form['fbs'])  # Fasting Blood Sugar (0/1)
        restecg = int(request.form['restecg'])  # Resting ECG (0-2)
        thalach = int(request.form['thalach'])  # Max Heart Rate
        exang = int(request.form['exang'])  # Exercise Angina (0/1)
        oldpeak = float(request.form['oldpeak'])  # ST Depression
        slope = int(request.form['slope'])  # Slope of ST Segment (0-2)
        ca = int(request.form['ca'])  # Number of Major Vessels (0-3)
        thal = int(request.form['thal'])  # Thalassemia (3, 6, 7)

        # One-hot encoding for Thalassemia (if needed)
        thal_3 = 1 if thal == 3 else 0
        thal_6 = 1 if thal == 6 else 0
        thal_7 = 1 if thal == 7 else 0

        # Final input array (ensure same feature order as during training)
        final_features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, 
                                    exang, oldpeak, slope, ca, thal_3, thal_6, thal_7]])

        # Make prediction
        prediction = model.predict(final_features)

        # Interpret the result
        risk_threshold = 0.5  # Adjust based on model output range
        if prediction[0] > risk_threshold:
            output = "⚠️ High risk of heart disease. Consult a doctor immediately."
        else:
            output = "✅ Low risk of heart disease. Keep maintaining a healthy lifestyle!"

        return render_template('index.html', prediction_text=output)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)



from flask import request

@app.route('/predict', methods=['POST'])
def predict():
    form_data = request.form
    print("User Input Data:", form_data)  # Debugging ke liye
