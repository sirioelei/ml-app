from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("iris_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = model.predict([data['features']])[0]
    prediction = int(prediction)

    return jsonify({'class': prediction})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
