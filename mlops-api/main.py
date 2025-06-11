from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import logging

app = FastAPI()
model = joblib.load("model.joblib")

# Logging
logging.basicConfig(filename='log.txt', level=logging.INFO)

class Input(BaseModel):
    features: list

@app.post("/predict")
def predict(data: Input):
    logging.info(f"Received: {data.features}")
    prediction = model.predict([data.features])
    return {"prediction": int(prediction[0])}

