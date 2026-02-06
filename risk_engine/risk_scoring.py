import joblib
import numpy as np


class RiskEngine:

    def __init__(self, model_path="model/anomaly_model.pkl"):
        """
        Load the trained anomaly model once.
        """
        self.model = joblib.load(model_path)

    def calculate_risk_score(self, features):
        """
        Convert anomaly score into a 0–100 risk score.
        """

        # Isolation Forest gives anomaly score
        anomaly_score = self.model.decision_function([features])[0]

        # Convert to positive risk scale
        risk_score = int((1 - anomaly_score) * 50)

        # Clamp score between 0 and 100
        risk_score = max(0, min(100, risk_score))

        return risk_score

    def make_decision(self, risk_score):
        """
        Adaptive authentication logic.
        """

        if risk_score < 30:
            return "ALLOW ✅"

        elif risk_score < 70:
            return "MFA REQUIRED ⚠️"

        else:
            return "BLOCK 🚨"

    def evaluate_login(self, features):
        """
        Full pipeline:
        features → risk → decision
        """

        risk_score = self.calculate_risk_score(features)
        decision = self.make_decision(risk_score)

        return {
            "risk_score": risk_score,
            "decision": decision
        }
