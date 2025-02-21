# Intelligent Real-Time Financial Anomaly Detection with Advanced MLOps


https://github.com/user-attachments/assets/0f2a9692-5368-47be-a203-39cd2c2ec041




## Overview
This project leverages **Machine Learning (ML)** and **MLOps** to detect fraudulent financial transactions in real-time. It integrates **Apache Kafka** for data streaming, **MLflow** for experiment tracking, **Kubeflow** for model deployment, and **Google BigQuery** for logging detected anomalies.

## Features
- **Real-time transaction ingestion** using Apache Kafka.
- **Anomaly detection** with Isolation Forest.
- **ML model training & tracking** via MLflow.
- **Automated deployment** using Kubeflow.
- **Logging and monitoring** with Google BigQuery (optional).

## Technologies Used
- **Python** (Pandas, NumPy, Scikit-learn, Joblib)
- **Apache Kafka** (Streaming transactions)
- **MLflow** (Experiment tracking)
- **Kubeflow** (Model deployment & automation)
- **Google BigQuery** (Anomaly logging)
- **Docker & Kubernetes** (Containerization & orchestration)

---

## Project Structure
```
├── data_ingestion.py          # Simulates real-time transactions & sends to Kafka
├── model_training.py          # Trains the Isolation Forest model & logs it to MLflow
├── anomaly_detection.py       # Consumes transactions & detects anomalies in real-time
├── deploy_pipeline.py         # Deploys the model using Kubeflow
├── requirements.txt           # Required dependencies
├── README.md                  # Project documentation
```

---

## Setup & Installation

### 1. Install Dependencies
Ensure Python is installed, then run:
```bash
pip install -r requirements.txt
```

### 2. Start Kafka
```bash
zookeeper-server-start.sh config/zookeeper.properties
kafka-server-start.sh config/server.properties
kafka-topics.sh --create --topic financial_transactions --bootstrap-server localhost:9092
```

### 3. Start MLflow Server
```bash
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 0.0.0.0 --port 5000
```

### 4. Train the Model
```bash
python model_training.py
```

### 5. Deploy Model with Kubeflow
```bash
kubectl apply -f pipeline.yaml
```

### 6. Run Real-time Anomaly Detection
```bash
python anomaly_detection.py
```

---

## How It Works
1. **Transactions are streamed** from Kafka in real-time.
2. **The trained ML model** predicts anomalies.
3. **Results are logged** into MLflow & optionally stored in BigQuery.
4. **Model is retrained automatically** through Kubeflow Pipelines.
5. **Continuous monitoring & deployment** ensure optimal performance.

---

## Future Enhancements
- **Integrate deep learning models** for better fraud detection.
- **Deploy as a cloud-based API** using Flask & Kubernetes.
- **Enhance monitoring** with Prometheus & Grafana.

🚀 **Ready to Detect Anomalies? Start Running the Scripts Now!** 🚀

