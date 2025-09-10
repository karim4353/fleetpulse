from fastapi import FastAPI
from pydantic import BaseModel
import os, time, joblib, json
app = FastAPI(title='FleetPulse Model Server')
MODEL_PATH = os.environ.get('MODEL_PATH','/ml/models/example_model.pkl')

class VehState(BaseModel):
    soc: float
    speed: float
    temperature_c: float

@app.on_event('startup')
def load_model():
    global model, mock
    model = None; mock = True
    if os.path.exists(MODEL_PATH):
        try:
            model = joblib.load(MODEL_PATH)
            mock = False
        except Exception:
            mock = True

@app.post('/predict/soh')
def predict_soh(s: VehState):
    ts = time.time()
    if not mock and model is not None:
        X = [[s.soc, s.speed, s.temperature_c]]
        p = model.predict(X)[0]
        mode = 'loaded'
    else:
        # fallback mocked prediction
        p = max(50.0, min(100.0, s.soc * 0.95 + 5.0))
        mode = 'mock'
    return {'prediction': float(p), 'model_version': mode, 'latency_ms': int((time.time()-ts)*1000)}

@app.post('/predict/rul')
def predict_rul(s: VehState):
    # Toy RUL: inverse of soh
    val = max(0.0, 100.0 - (s.soc + 0.5))
    return {'prediction': float(val), 'model_version':'rul-mock', 'latency_ms': 1}
