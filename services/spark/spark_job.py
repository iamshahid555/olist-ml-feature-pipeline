from pyspark.sql import SparkSession

from config import (
    APP_NAME,
    MASTER,
    RAW_DATA_PATH,
    PROCESSED_DATA_PATH,
    POSTGRES_JDBC_DRIVER,
)

from feature_engineering import create_features
from preprocessing import clean_orders
from postgres_writer import write_to_postgres


def main():

    spark = (
        SparkSession.builder
        .appName(APP_NAME)
        .master(MASTER)
        .config("spark.jars", POSTGRES_JDBC_DRIVER)
        .getOrCreate()
    )

    print("Reading dataset...")

    df = spark.read.csv(
        RAW_DATA_PATH,
        header=True,
        inferSchema=True
    )

    print(f"Original rows: {df.count()}")

    df = clean_orders(df)

    print(f"Rows after preprocessing: {df.count()}")

    features = create_features(df)

    print("Generated features")

    features.printSchema()

    features.show(5, truncate=False)

    features.write.mode("overwrite").parquet(PROCESSED_DATA_PATH)

    write_to_postgres(features)

    print("Features saved successfully")

    spark.stop()


if __name__ == "__main__":
    main()