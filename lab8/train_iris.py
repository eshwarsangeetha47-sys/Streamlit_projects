
from pathlib import Path

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the Iris dataset
X, y = load_iris(return_X_y=True)

# Train the machine-learning model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Save the model inside the lab8 folder
model_path = Path(__file__).parent / "model.pkl"
joblib.dump(model, model_path)

print("Model trained and saved successfully!")
