import os
import joblib
import numpy as np

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
MODELS_DIR = os.path.join(ROOT_DIR, "model")
MODEL_PATH = os.path.join(MODELS_DIR, "model.joblib")
SCALER_PATH = os.path.join(MODELS_DIR, "scaler.joblib")

def load_model_and_scaler():
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    return model, scaler

def predict(features):
    model, scaler = load_model_and_scaler()
    features = np.array(features).reshape(1, -1)
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)
    return int(prediction[0])