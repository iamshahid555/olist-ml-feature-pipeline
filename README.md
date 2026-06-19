# 🚀 Olist ML Feature Pipeline

> Production-grade batch data pipeline that ingests 1M+ e-commerce records and delivers ML-ready feature tables via REST API — built with Apache Kafka, Spark, Airflow, HDFS, PostgreSQL & FastAPI, fully containerised with Docker Compose.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker)
![Kafka](https://img.shields.io/badge/Apache-Kafka-231F20?logo=apachekafka)
![Spark](https://img.shields.io/badge/Apache-Spark-E25A1C?logo=apachespark)
![Airflow](https://img.shields.io/badge/Apache-Airflow-017CEE?logo=apacheairflow)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📐 Architecture

| Layer | Technology | Role |
|---|---|---|
| Ingestion | Apache Kafka | Monthly batch ingestion |
| Raw Storage | HDFS | Distributed file storage |
| Processing | Apache Spark | Quarterly batch processing & feature engineering |
| Feature Store | PostgreSQL | Processed feature tables |
| Delivery | FastAPI | REST API serving feature sets to ML app |
| Orchestration | Apache Airflow | DAG scheduling & monitoring |
| IaC | Docker Compose | Fully containerised microservices |

---

## 🗂️ Project Structure
olist-ml-feature-pipeline/

│

├── services/

│   ├── kafka/               # Kafka producer & consumer configs

│   ├── airflow/

│   │   └── dags/            # Airflow DAG definitions

│   ├── spark/               # Spark batch processing jobs

│   ├── postgres/            # Schema & init scripts

│   └── fastapi/             # REST API for feature delivery

│

├── data/

│   ├── raw/                 # Raw ingested CSV data

│   └── processed/           # Aggregated feature tables

│

├── config/                  # Shared configuration files

├── docker-compose.yml       # Full infrastructure definition

├── .gitignore

└── README.md
---

## 🛠️ Tech Stack

- **Ingestion:** Apache Kafka
- **Storage:** HDFS, PostgreSQL
- **Processing:** Apache Spark
- **Orchestration:** Apache Airflow
- **Delivery:** FastAPI
- **IaC:** Docker Compose
- **Version Control:** Git & GitHub
- **Language:** Python 3.11

---

## 📦 Dataset

[Olist Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) — 1M+ timestamped order records across 9 CSV files covering orders, customers, products, payments, reviews and sellers.

---

## ⚡ Getting Started

```bash
# Clone the repository
git clone https://github.com/iamshahid555/olist-ml-feature-pipeline.git
cd olist-ml-feature-pipeline

# Start all microservices
docker-compose up -d

# Check running containers
docker ps
```

---

## 🔄 Pipeline Schedule

| Stage | Frequency | Description |
|---|---|---|
| Data Ingestion | Monthly | Kafka producer reads Olist CSVs |
| Batch Processing | Quarterly | Spark aggregates & engineers features |
| Feature Delivery | On-demand | FastAPI serves feature tables via REST |

---

## 🔒 Security & Reliability

- TLS/SSL encrypted inter-service communication
- Role-Based Access Control (RBAC) on PostgreSQL
- Audit logging via ELK/EFK stack
- Kafka durable log replication & exactly-once delivery
- Airflow retry logic & failure alerts
- Idempotent Spark processing

---

## 🎓 Course

**IU International University of Applied Sciences**
DLMDSEDE02 — Data Engineering Portfolio Project
