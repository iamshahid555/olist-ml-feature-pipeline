# Olist ML Feature Pipeline

A production-grade batch data pipeline that ingests 1M+ e-commerce records from the Olist Brazilian E-Commerce dataset and delivers ML-ready feature tables via REST API.

## Architecture

| Layer | Technology | Role |
|---|---|---|
| Ingestion | Apache Kafka | Monthly batch ingestion |
| Raw Storage | HDFS | Distributed file storage |
| Processing | Apache Spark | Quarterly batch processing & feature engineering |
| Feature Store | PostgreSQL | Processed feature tables |
| Delivery | FastAPI | REST API serving feature sets to ML app |
| Orchestration | Apache Airflow | DAG scheduling & monitoring |
| IaC | Docker Compose | Fully containerised microservices |

## Tech Stack
- Apache Kafka · Apache Spark · Apache Airflow
- HDFS · PostgreSQL · FastAPI
- Docker Compose · Python · Git

## Dataset
[Olist Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) — 1M+ timestamped order records across 9 CSV files.

## Project Structure
olist-ml-feature-pipeline/

├── services/

│   ├── kafka/          # Kafka producer & consumer configs

│   ├── airflow/        # DAGs and Airflow configuration

│   ├── spark/          # Spark batch processing jobs

│   ├── postgres/       # Schema & init scripts

│   └── fastapi/        # REST API for feature delivery

├── data/

│   ├── raw/            # Raw ingested CSV data

│   └── processed/      # Aggregated feature tables

├── config/             # Shared configuration files

└── docker-compose.yml  # Full infrastructure definition
## Getting Started
```bash
git clone https://github.com/YOUR_USERNAME/olist-ml-feature-pipeline.git
cd olist-ml-feature-pipeline
docker-compose up -d
```

## Course
IU International University of Applied Sciences — DLMDSEDE02 Data Engineering
