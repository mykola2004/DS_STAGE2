from flask import Flask, request, jsonify
from project_package.model import predict

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict_endpoint():
    try:
        input_json = request.get_json()
        features = input_json["features"]
        prediction = predict(features)
        return jsonify({"prediction": int(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)