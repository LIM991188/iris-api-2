from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
# Load the classic Iris dataset (4 features, 3 classes)
X, y = load_iris(return_X_y=True)
model = RandomForestClassifier()
model.fit(X, y)
# Save the trained model to a file
joblib.dump(model, "model.joblib")
print("Model saved to model.joblib")