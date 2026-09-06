from pathlib import Path

import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline


# --------------------------------------------------
# Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "Titanic-Dataset.csv"


# --------------------------------------------------
# Load and prepare Titanic dataset
# --------------------------------------------------

df = pd.read_csv(DATASET_PATH)

df = df[["Age", "Sex", "Survived"]]

df = df.dropna()

df["SexEncoded"] = df["Sex"].map(
    {
        "male": 0,
        "female": 1
    }
)


# --------------------------------------------------
# Feature and Target
# --------------------------------------------------

X = df[
    [
        "Age",
        "SexEncoded"
    ]
]

y = df["Survived"]


# --------------------------------------------------
# Create and train model
# --------------------------------------------------

model = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=15)
)

model.fit(X, y)


# --------------------------------------------------
# Prediction function
# --------------------------------------------------

def predict_survival(age: float, sex: str):

    if sex == "male":
        sex_encoded = 0
    else:
        sex_encoded = 1

    input_data = pd.DataFrame(
        [
            {
                "Age": age,
                "SexEncoded": sex_encoded
            }
        ]
    )

    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]

    survival_probability = probabilities[1] * 100
    death_probability = probabilities[0] * 100

    if prediction == 1:
        prediction_text = "survived"
    else:
        prediction_text = "did not survive"

    result = {
        "age": age,
        "sex": sex,
        "prediction": prediction_text,
        "survival_probability": round(
            survival_probability,
            2
        ),
        "death_probability": round(
            death_probability,
            2
        )
    }

    return result
