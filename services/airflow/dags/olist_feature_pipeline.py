from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="olist_feature_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["olist", "data-engineering"],
) as dag:

    kafka_ingestion = BashOperator(
        task_id="kafka_ingestion",
        bash_command=(
    "cd /opt/airflow/project && "
    "python services/kafka/producer.py"
),
        env={
            "KAFKA_BOOTSTRAP_SERVERS": "kafka:29092",
        },
    )

    spark_feature_pipeline = BashOperator(
        task_id="spark_feature_pipeline",
        bash_command=(
            "cd /opt/airflow/project && "
            "/home/airflow/.local/bin/spark-submit "
            "--jars /opt/airflow/project/jars/postgresql-42.7.13.jar "
            "services/spark/spark_job.py"
        ),
        env={

            "POSTGRES_HOST": "postgres",

            "PYSPARK_PYTHON": "/home/airflow/.local/bin/python3",

            "PYSPARK_DRIVER_PYTHON": "/home/airflow/.local/bin/python3",

        },
    )

    kafka_ingestion >> spark_feature_pipeline