import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os


def load_data():
    """
    Loads the synthetic login dataset.
    """
    df = pd.read_csv("login_behavior.csv")
    return df


def train_isolation_forest(X):
    """
    Train Isolation Forest for anomaly detection.
    contamination defines expected attack %.
    """
    model = IsolationForest(
        n_estimators=100,
        contamination=0.2,   # because we generated ~20% attacks
        random_state=42
    )

    model.fit(X)
    return model


def evaluate_model(model, X, y):
    """
    Simple evaluation so you can SHOW results to judges.
    IsolationForest outputs:
        -1 = anomaly
         1 = normal
    We'll convert to:
        1 = attack
        0 = normal
    """

    predictions = model.predict(X)

    predictions = [1 if p == -1 else 0 for p in predictions]

    accuracy = (predictions == y).mean()

    print(f"\n✅ Model Accuracy (approx): {accuracy*100:.2f}%")

    # Optional deeper insight
    from sklearn.metrics import classification_report
    print("\nClassification Report:")
    print(classification_report(y, predictions))


def save_model(model):
    """
    Saves trained model to disk.
    """
    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/anomaly_model.pkl")

    print("\n✅ Model saved as model/anomaly_model.pkl")


if __name__ == "__main__":

    print("Loading dataset...")
    df = load_data()

    X = df.drop("label", axis=1)
    y = df["label"]

    print("Training Isolation Forest...")
    model = train_isolation_forest(X)

    evaluate_model(model, X, y)

    save_model(model)

    print("\n🔥 Training Complete!")
