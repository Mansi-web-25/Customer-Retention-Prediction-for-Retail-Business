import joblib

def predict_churn(input_data, model_path='xgb_model.pkl'):
    model = joblib.load(model_path)
    prediction = model.predict(input_data)
    return prediction
