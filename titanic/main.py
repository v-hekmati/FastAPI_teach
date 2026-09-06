from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

from schemas import PassengerInput
from model import predict_survival


# --------------------------------------------------
# Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
HTML_PATH = BASE_DIR / "static" / "index.html"


# --------------------------------------------------
# FastAPI application
# --------------------------------------------------

app = FastAPI()


# --------------------------------------------------
# Web page
# --------------------------------------------------

@app.get("/")
def home():
    return FileResponse(HTML_PATH)


# --------------------------------------------------
# Prediction API
# --------------------------------------------------

@app.post("/predict")
def predict(passenger: PassengerInput):

    result = predict_survival(
        age=passenger.age,
        sex=passenger.sex
    )

    return result
