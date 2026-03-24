import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.datasets import load_wine
mlflow.set_tracking_uri("sqlite:///mlflow.db")


# ID runu z najlepszym modelem
RUN_ID = "e9db5f690bc84c38b2abeb3c16da02e1"

# Załadowanie modelu
model = mlflow.sklearn.load_model(f"runs:/{RUN_ID}/model")

# Załadowanie danych do testu
wine = load_wine()

# Test na pierwszej próbce
X_sample = wine.data[0].reshape(1, -1)
expected_class = wine.target[0]

pred = model.predict(X_sample)
prob = model.predict_proba(X_sample)

print("Testowanie modelu:")
print(f"Przewidywana klasa: {pred[0]}")
print(f"Prawdopodobieństwa klas: {prob[0]}")
print(f"Oczekiwana klasa: {expected_class}")