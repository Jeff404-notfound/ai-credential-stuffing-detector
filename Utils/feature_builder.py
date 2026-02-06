import numpy as np


class FeatureBuilder:
    """
    Transforms raw login inputs into a model-ready feature vector.
    Ensures consistency between training and inference.
    """

    def __init__(self):
        # Feature order MUST match training data
        self.feature_order = [
            "login_attempts_per_min",
            "failed_login_ratio",
            "ip_changes",
            "device_changes",
            "geo_distance_km"
        ]

    def build_feature_vector(
        self,
        login_attempts,
        failed_ratio,
        ip_changes,
        device_changes,
        geo_distance
    ):
        """
        Converts inputs into a structured numpy array.
        """

        features = np.array([
            login_attempts,
            failed_ratio,
            ip_changes,
            device_changes,
            geo_distance
        ], dtype=float)

        return features
