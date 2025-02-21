import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import IsolationForest

# Load training dataset
data = pd.read_csv("financial_transactions.csv")
X = data[['amount', 'transaction_type', 'account_balance']]

# Train model
model = IsolationForest(contamination=0.02, random_state=42)
model.fit(X)

# Save model
joblib.dump(model, "anomaly_detection_model.pkl")
print("Model trained and saved successfully.")