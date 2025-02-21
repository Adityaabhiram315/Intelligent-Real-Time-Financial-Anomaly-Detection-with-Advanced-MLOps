## Intelligent Real-Time Financial Anomaly Detection with Advanced MLOps

This project aims to detect fraudulent financial transactions in real-time using machine learning and MLOps tools like Apache Kafka, BigQuery, Kubeflow, and MLflow.

### Project Structure:
- **data_ingestion.py** - Simulates real-time transactions and sends them to Kafka.
- **model_training.py** - Trains an Isolation Forest model and saves it for deployment.
- **anomaly_detection.py** - Consumes transactions, predicts anomalies, and logs results to MLflow.
- **deploy_pipeline.py** - Deploys the model using Kubeflow for real-time predictions.
- **requirements.txt** - Dependencies required for the project.
- **README.md** - Documentation for setting up and running the project.

---

### 1. Data Ingestion (`data_ingestion.py`)

from kafka import KafkaProducer
import json
import time
import random

def generate_transaction():
    return {
        "id": random.randint(1000, 9999),
        "amount": round(random.uniform(1, 10000), 2),
        "transaction_type": random.choice([0, 1]),
        "account_balance": round(random.uniform(1000, 50000), 2)
    }

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

while True:
    transaction = generate_transaction()
    producer.send('financial_transactions', value=transaction)
    print(f"Sent transaction: {transaction}")
    time.sleep(2)
