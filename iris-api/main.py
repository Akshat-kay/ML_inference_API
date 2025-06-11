from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model.joblib")

class IrisInput(BaseModel):
    features: list

@app.post("/predict")
def predict(data: IrisInput):
    pred = model.predict([data.features])
    return {"prediction": int(pred[0])}

