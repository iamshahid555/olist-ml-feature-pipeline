# Olist ML Feature Pipeline

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker)
![Kafka](https://img.shields.io/badge/Apache-Kafka-231F20?logo=apachekafka)
![Spark](https://img.shields.io/badge/Apache-Spark-E25A1C?logo=apachespark)
![Airflow](https://img.shields.io/badge/Apache-Airflow-017CEE?logo=apacheairflow)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi)

A production-inspired batch data engineering project that demonstrates
an end-to-end machine learning feature pipeline using Apache Kafka,
Apache Spark, PostgreSQL, FastAPI, and Docker Compose, with Apache
Airflow being implemented for workflow orchestration.

## Overview

Olist ML Feature Pipeline is a batch-processing data engineering project
that builds a reliable, scalable, and maintainable backend for machine
learning feature generation. The platform uses the Olist Brazilian
E-Commerce dataset and transforms raw transactional data into ML-ready
feature tables through a reproducible microservices architecture.

The project follows Infrastructure as Code (IaC) principles and uses
Docker Compose to deploy isolated services for ingestion, storage,
processing, orchestration, and delivery.

## Implementation Status

This project is being developed incrementally following an
infrastructure-first approach.

  Component                               Status
  ---------------------------------- ----------------
  Project Structure                         ✅
  Docker Compose                            ✅
  PostgreSQL Infrastructure                 ✅
  Dataset Preparation                       ✅
  Apache Kafka Producer                     ✅
  Apache Kafka Consumer                     ✅
  Apache Spark Preprocessing                ✅
  Apache Spark Feature Engineering          ✅
  Apache Parquet Feature Store              ✅
  PostgreSQL Feature Store                  ✅
  FastAPI                                   ✅
  Apache Airflow                      🔄 In Progress

------------------------------------------------------------------------

## Project Goals

-   Build a reproducible batch-processing data platform
-   Implement a modular microservices-based architecture
-   Perform feature engineering using Apache Spark
-   Orchestrate workflows with Apache Airflow
-   Store engineered feature tables in PostgreSQL
-   Store processed feature data in Apache Parquet
-   Deliver feature data through a FastAPI REST API
-   Apply reliability, scalability, and maintainability principles
-   Demonstrate an end-to-end data engineering workflow

------------------------------------------------------------------------

## Technology Stack

  -----------------------------------------------------------------------
  Component               Technology              Purpose
  ----------------------- ----------------------- -----------------------
  Data Ingestion          Apache Kafka            Data ingestion and
                                                  message streaming

  Raw Data Storage        CSV Files               Storage of the raw
                                                  Olist dataset

  Processing Engine       Apache Spark            Data preprocessing and
                                                  feature engineering

  Processed Data Storage  Apache Parquet          Storage of engineered
                                                  feature data

  Feature Store           PostgreSQL              Persistent storage of
                                                  engineered features

  API Layer               FastAPI                 REST API for feature
                                                  delivery

  Workflow Orchestration  Apache Airflow          Pipeline scheduling and
                                                  workflow management

  Containerization        Docker Compose          Reproducible
                                                  infrastructure

  Version Control         Git & GitHub            Source control and
                                                  project management
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Architecture

The architecture diagram for the batch-processing pipeline is available
in `docs/architecture.svg`.

The current implementation uses Apache Kafka for data ingestion, Apache
Spark for preprocessing and feature engineering, Apache Parquet and
PostgreSQL for feature storage, and FastAPI for feature delivery. Apache
Airflow is being implemented as the workflow orchestration layer.

The current data-processing flow is:

``` text
Olist CSV Dataset
       │
       ├──────────────► Apache Kafka
       │                    │
       │                    ▼
       │              Kafka Consumer
       │
       ▼
Apache Spark
       │
       ├── Data Preprocessing
       └── Feature Engineering
              │
              ├──────────────► Apache Parquet
              │
              └──────────────► PostgreSQL Feature Store
                                      │
                                      ▼
                                  FastAPI
```

Kafka ingestion and Spark processing are currently implemented as
separate pipeline components. Apache Airflow will be added to
orchestrate the workflow.

------------------------------------------------------------------------

## Repository Structure

``` text
olist-ml-feature-pipeline/
│
├── config/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│   ├── architecture.svg
│   └── screenshots/
│
├── services/
│   ├── airflow/
│   │   └── dags/
│   │
│   ├── fastapi/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── requirements.txt
│   │   └── schema.py
│   │
│   ├── kafka/
│   │   ├── producer.py
│   │   ├── consumer.py
│   │   └── config.py
│   │
│   ├── postgres/
│   │   ├── init.sql
│   │   ├── db.py
│   │   └── __init__.py
│   │
│   └── spark/
│       ├── spark_job.py
│       ├── preprocessing.py
│       ├── feature_engineering.py
│       ├── postgres_writer.py
│       ├── config.py
│       ├── requirements.txt
│       └── __init__.py
│
├── jars/
│   └── postgresql-42.7.13.jar
│
├── docker-compose.yml
├── .env
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

### Folder Description

  -------------------------------------------------------------------------------
  Folder                Description
  --------------------- ---------------------------------------------------------
  `config`              Shared project configuration files

  `data`                Contains the raw Olist dataset and processed outputs
                        generated by the pipeline

  `docs`                Architecture diagrams and project documentation

  `services/airflow`    Workflow orchestration and scheduling

  `services/fastapi`    REST API for serving engineered features from PostgreSQL

  `services/kafka`      Kafka producer and consumer components for data ingestion

  `services/postgres`   PostgreSQL database initialization and feature store
                        configuration

  `services/spark`      Spark preprocessing and feature engineering pipeline

  `jars`                PostgreSQL JDBC driver used for Spark database
                        integration
  -------------------------------------------------------------------------------

------------------------------------------------------------------------

## Development Roadmap

### Phase 1 - Completed

-   Architecture design
-   Technology selection
-   Dataset selection
-   Infrastructure planning

### Phase 2 - Completed

-   Docker Compose environment
-   Kafka producer implementation
-   Kafka consumer implementation
-   Spark preprocessing pipeline
-   Spark feature engineering pipeline
-   Apache Parquet feature storage
-   PostgreSQL feature store integration
-   FastAPI REST API for feature serving

### Phase 3 - In Progress

-   Apache Airflow workflow orchestration - In Progress
-   End-to-end pipeline validation
-   Performance testing
-   Final documentation

------------------------------------------------------------------------

## Dataset

**Dataset:** Olist Brazilian E-Commerce Dataset

**Source:** [Olist Brazilian E-Commerce Dataset -
Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

> **Note:** The Olist dataset is intentionally not included in this
> repository because of its size. Download the dataset from Kaggle and
> extract all CSV files into `data/raw/` before running the project.

The complete Olist Brazilian E-Commerce dataset is stored locally under
`data/raw/`. Processed datasets and engineered feature tables generated
during pipeline execution are written to `data/processed/`.

------------------------------------------------------------------------

## Feature Engineering

The Apache Spark feature engineering pipeline generates delivery,
processing, temporal, and order-status features from the Olist order
data.

The generated features include:

-   `delivery_time_days`
-   `carrier_delivery_days`
-   `delivery_delay_days`
-   `processing_time_days`
-   `purchase_year`
-   `purchase_month`
-   `purchase_day`
-   `purchase_weekday`
-   `is_delivered`

The engineered features are stored in Apache Parquet and PostgreSQL.

------------------------------------------------------------------------

## PostgreSQL Feature Store

The PostgreSQL feature store contains the engineered order-level feature
table:

`orders_features`

The table stores order identifiers, order status and timestamps,
engineered delivery and processing metrics, temporal features, and the
delivery-status indicator.

------------------------------------------------------------------------

## FastAPI Feature Service

The FastAPI service provides access to engineered features stored in
PostgreSQL.

### Available Endpoints

  -------------------------------------------------------------------------
  Method             Endpoint                 Description
  ------------------ ------------------------ -----------------------------
  `GET`              `/`                      Returns an API status message

  `GET`              `/health`                Checks API and PostgreSQL
                                              connectivity

  `GET`              `/features/{order_id}`   Retrieves engineered features
                                              for a specific order

  `GET`              `/docs`                  Opens the interactive Swagger
                                              API documentation
  -------------------------------------------------------------------------

Example:

``` bash
curl http://127.0.0.1:8000/features/000229ec398224ef6ca0657da4fc703e
```

The API returns the engineered feature values for the requested order
when the order exists in the PostgreSQL feature store.

------------------------------------------------------------------------

## Current Project Status

The project currently includes:

-   Apache Kafka producer and consumer components
-   Apache Spark preprocessing and feature engineering
-   Apache Parquet feature storage
-   PostgreSQL feature store integration
-   FastAPI feature-serving API

Apache Airflow is currently being implemented for workflow
orchestration. After Airflow integration, the remaining work includes
complete end-to-end pipeline validation, performance testing, and final
documentation.

------------------------------------------------------------------------

## Prerequisites

Before running the project, install:

-   Python 3.13+
-   OpenJDK 17
-   Docker Desktop
-   Git
-   Homebrew (macOS)

------------------------------------------------------------------------

## Local Development

Clone the repository:

``` bash
git clone https://github.com/iamshahid555/olist-ml-feature-pipeline.git
cd olist-ml-feature-pipeline
```

Create and activate a Python virtual environment:

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

``` bash
pip install -r requirements.txt
pip install -r services/spark/requirements.txt
```

Start the infrastructure:

``` bash
docker compose up -d
```

Run the Kafka producer and consumer:

``` bash
python services/kafka/producer.py
python services/kafka/consumer.py
```

Run the Spark pipeline:

``` bash
python services/spark/spark_job.py
```

Start the FastAPI service:

``` bash
uvicorn services.fastapi.main:app --host 0.0.0.0 --port 8000
```

Once the PostgreSQL feature store is populated, the API is available at:

`http://localhost:8000`

Interactive API documentation is available at:

`http://localhost:8000/docs`

The service provides `GET /` for an API status message, `GET /health`
for database connectivity, and `GET /features/{order_id}` to retrieve
engineered features for a specific order.

> **Note:** Apache Airflow orchestration is currently under
> implementation and will be integrated into the execution workflow.

------------------------------------------------------------------------

## Project Highlights

-   Modular microservices architecture
-   Docker Compose-based Infrastructure as Code (IaC)
-   Apache Kafka producer and consumer
-   Apache Spark preprocessing pipeline
-   Apache Spark feature engineering
-   Apache Parquet feature storage
-   PostgreSQL feature store
-   FastAPI REST API for feature serving

------------------------------------------------------------------------

## Pipeline Workflow

The currently implemented processing workflow is:

``` text
Olist CSV Dataset
       │
       ├──────────────► Apache Kafka Producer
       │                    │
       │                    ▼
       │              Apache Kafka Topic
       │                    │
       │                    ▼
       │              Kafka Consumer
       │
       ▼
Apache Spark
       │
       ├── Data Preprocessing
       └── Feature Engineering
              │
              ├──────────────► Apache Parquet
              │
              └──────────────► PostgreSQL Feature Store
                                      │
                                      ▼
                                  FastAPI REST API
```

Apache Airflow will be added to orchestrate the execution of the
pipeline components.

------------------------------------------------------------------------

## Academic Context

**Course:** DLMDSEDE02 - Data Engineering Portfolio Project

**Institution:** IU International University of Applied Sciences

### Focus Areas

-   Batch Processing
-   Data Engineering
-   Microservices
-   Infrastructure as Code
-   Feature Engineering
-   Machine Learning Pipelines

------------------------------------------------------------------------

## Future Enhancements

-   Orchestrate the complete pipeline using Apache Airflow
-   Extend the FastAPI service with list, filter, and pagination
    endpoints
-   Add monitoring and structured logging
-   Add automated testing
-   Perform pipeline performance evaluation
-   Deploy the pipeline to a cloud platform

------------------------------------------------------------------------

## License

MIT License
