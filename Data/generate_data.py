import pandas as pd
import numpy as np

# For reproducibility (important in AI systems)
np.random.seed(42)


def generate_normal_users(n=800):
    """
    Simulates normal human login behavior.
    """
    data = pd.DataFrame({
        "login_attempts_per_min": np.random.randint(1, 5, n),
        "failed_login_ratio": np.random.uniform(0.0, 0.3, n),
        "ip_changes": np.random.randint(0, 2, n),
        "device_changes": np.random.randint(0, 2, n),
        "geo_distance_km": np.random.uniform(0, 50, n)
    })

    data["label"] = 0  # 0 = normal
    return data


def generate_attack_users(n=200):
    """
    Simulates credential stuffing attack behavior.
    """
    data = pd.DataFrame({
        "login_attempts_per_min": np.random.randint(20, 120, n),
        "failed_login_ratio": np.random.uniform(0.6, 1.0, n),
        "ip_changes": np.random.randint(3, 10, n),
        "device_changes": np.random.randint(2, 6, n),
        "geo_distance_km": np.random.uniform(500, 10000, n)
    })

    data["label"] = 1  # 1 = attack
    return data


def generate_dataset():
    normal = generate_normal_users()
    attacks = generate_attack_users()

    dataset = pd.concat([normal, attacks], ignore_index=True)

    # Shuffle the dataset (VERY important)
    dataset = dataset.sample(frac=1).reset_index(drop=True)

    return dataset


if __name__ == "__main__":
    df = generate_dataset()

    # Save dataset
    df.to_csv("login_behavior.csv", index=False)

    print("✅ Dataset generated successfully!")
    print(df.head())
    print("\nClass Distribution:")
    print(df["label"].value_counts())
