import pandas as pd
import numpy as np
import joblib
import mlflow
import mlflow.sklearn
from kafka import KafkaConsumer
from json import loads

# Load pre-trained anomaly detection model
model = joblib.load("anomaly_detection_model.pkl")

# Kafka Consumer to receive real-time financial transactions
def consume_transactions():
    consumer = KafkaConsumer(
        'financial_transactions',
        bootstrap_servers=['localhost:9092'],
        value_deserializer=lambda x: loads(x.decode('utf-8'))
    )
    
    print("Listening for transactions...")
    
    for message in consumer:
        transaction = message.value
        data = np.array([transaction['amount'], transaction['transaction_type'], transaction['account_balance']]).reshape(1, -1)
        
        # Predict anomaly
        prediction = model.predict(data)
        anomaly_status = "Anomalous" if prediction == -1 else "Normal"
        
        print(f"Transaction: {transaction}, Status: {anomaly_status}")
        
        # Logging anomaly to MLflow
        mlflow.log_param("Transaction_ID", transaction['id'])
        mlflow.log_param("Amount", transaction['amount'])
        mlflow.log_param("Prediction", anomaly_status)

if __name__ == "__main__":
    consume_transactions()