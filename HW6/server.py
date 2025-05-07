import os
import joblib
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

MODEL_DIR = os.path.join(os.path.dirname(__file__), 'model')
MODEL_PATH = os.path.join(MODEL_DIR, 'model.joblib')
SCALER_PATH = os.path.join(MODEL_DIR, 'scaler.joblib')

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "ok"})

@app.route("/invocations", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = np.array(data["instances"])
        scaled = scaler.transform(features)
        predictions = model.predict(scaled)
        return jsonify({"predictions": predictions.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)