# Olist ML Feature Pipeline

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker)
![Kafka](https://img.shields.io/badge/Apache-Kafka-231F20?logo=apachekafka)
![Spark](https://img.shields.io/badge/Apache-Spark-E25A1C?logo=apachespark)
![Airflow](https://img.shields.io/badge/Apache-Airflow-017CEE?logo=apacheairflow)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql)

## Overview

Olist ML Feature Pipeline is a batch-processing data engineering project that builds a reliable, scalable, and maintainable backend for machine learning feature generation. The platform uses the Olist Brazilian E-Commerce dataset and transforms raw transactional data into ML-ready feature tables through a reproducible microservices architecture.

The project follows Infrastructure as Code (IaC) principles and uses Docker Compose to deploy isolated services for ingestion, storage, processing, orchestration, and delivery.

---

## Project Goals

- Build a reproducible batch-processing data platform
- Implement a microservices-based architecture
- Perform large-scale feature engineering using Apache Spark
- Orchestrate workflows with Apache Airflow
- Store processed feature tables in PostgreSQL
- Deliver feature data through a FastAPI service
- Apply reliability, scalability, and maintainability principles

---

## Technology Stack

| Component | Technology | Purpose |
|------------|------------|------------|
| Data Ingestion | Apache Kafka | Scheduled data ingestion |
| Raw Data Storage | HDFS | Distributed storage layer |
| Processing Engine | Apache Spark | Feature engineering and aggregation |
| Workflow Orchestration | Apache Airflow | Pipeline scheduling and management |
| Feature Store | PostgreSQL | Storage of processed features |
| API Layer | FastAPI | Feature delivery service |
| Containerization | Docker Compose | Infrastructure as Code |
| Version Control | Git & GitHub | Source control and collaboration |

---

## Architecture

Architecture diagram available in the `docs/` directory.

---

## Repository Structure

```text
olist-ml-feature-pipeline/
│
├── airflow/
│   └── dags/
│
├── src/
│   ├── producer/
│   ├── spark/
│   └── api/
│
├── postgres/
├── datasets/
├── docs/
│   ├── architecture.png
│   └── screenshots/
│
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

## Development Roadmap

### Phase 1 - Completed
- Architecture design
- Technology selection
- Dataset selection
- Infrastructure planning

### Phase 2 - In Progress
- Docker Compose environment
- Kafka ingestion service
- Spark batch processing jobs
- PostgreSQL feature store
- FastAPI service
- Airflow orchestration

### Phase 3 - Planned
- End-to-end pipeline validation
- Performance testing
- Documentation and project reflection

### Folder Description

| Folder | Description |
|----------|----------|
| airflow | Workflow orchestration and DAG definitions |
| src/producer | Kafka ingestion services |
| src/spark | Batch processing and feature engineering jobs |
| src/api | FastAPI feature delivery service |
| postgres | Database initialization and schema scripts |
| datasets | Source datasets used by the pipeline |
| docs | Architecture diagrams, screenshots, and project evidence |

---

## Dataset

**Dataset:** Olist Brazilian E-Commerce Dataset

**Source:**  
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

The dataset contains more than one million timestamped e-commerce records and serves as the source for feature engineering and sales forecasting use cases.

---

## Current Project Status

This repository is currently in the implementation phase. The architecture and project design have been finalized, and the microservices are being developed incrementally. Progress and screenshots will be documented throughout the implementation process.

---

## Local Development

```bash
git clone https://github.com/iamshahid555/olist-ml-feature-pipeline.git
cd olist-ml-feature-pipeline
```

Implementation is currently under active development.

---

## Academic Context

**Course:** DLMDSEDE02 – Data Engineering Portfolio Project  
**Institution:** IU International University of Applied Sciences

### Focus Areas

- Batch Processing
- Data Engineering
- Microservices
- Infrastructure as Code
- Feature Engineering
- Machine Learning Pipelines

---

## License

MIT License