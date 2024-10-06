import pickle
import numpy as np
import pandas as pd

# Backend: Function to load model and make predictions
def load_model():
    with open('Random_Forests.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Prediction function
def predict_loan_default(input_data):
    model = load_model()
    # Make prediction using the input data (it should be a DataFrame or array)
    prediction = model.predict(input_data)[0]
    return prediction
