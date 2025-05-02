import requests

def test_api_predict():
    url = "http://localhost:5000/predict"
    data = {"features": [5.1, 3.5, 1.4, 9.0]}
    response = requests.post(url, json=data)

    assert response.status_code == 200

    json_data = response.json()
    assert "prediction" in json_data
    assert isinstance(json_data["prediction"], int)
