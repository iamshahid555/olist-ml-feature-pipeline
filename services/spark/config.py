import os

RAW_DATA_PATH = "data/raw/olist_orders_dataset.csv"

PROCESSED_DATA_PATH = "data/processed/orders_features.parquet"

APP_NAME = "Olist Feature Engineering"

MASTER = "local[*]"

# PostgreSQL Configuration

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = "5432"

POSTGRES_DATABASE = "feature_store"

POSTGRES_USER = "admin"
POSTGRES_PASSWORD = "admin123"

POSTGRES_TABLE = "orders_features"

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

POSTGRES_JDBC_DRIVER = str(
    PROJECT_ROOT / "jars" / "postgresql-42.7.13.jar"
)