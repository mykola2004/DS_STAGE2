from project_package.model import load_model_and_scaler, predict

def test_load_model_and_scaler():
    model, scaler = load_model_and_scaler()
    assert model != None
    assert scaler != None

def test_predict():
    features = [5.1, 3.5, 1.4, 0.2]
    result = predict(features)
    assert isinstance(result, int)