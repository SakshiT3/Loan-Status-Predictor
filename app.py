# app.py

from flask import Flask, request, render_template
import pickle
import numpy as np

# Load the trained model
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
        # Extract and convert form data to appropriate types
        int_features = [int(x) for x in request.form.values()]
        final_features = [np.array(int_features)]

        # Make prediction
        prediction = model.predict(final_features)

        # Map model output to loan status
        output = 'Approved' if prediction[0] == 1 else 'Rejected'

        return render_template('index.html', prediction_text='Loan Status: {}'.format(output))
    
    except Exception as e:
        return render_template('index.html', prediction_text='Error: {}'.format(str(e)))

if __name__ == "__main__":
    app.run(debug=True)
