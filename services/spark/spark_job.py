from pyspark.sql import SparkSession

from config import (
    APP_NAME,
    MASTER,
    RAW_DATA_PATH,
    PROCESSED_DATA_PATH,
)

from feature_engineering import create_features


def main():

    spark = (
        SparkSession.builder
        .appName(APP_NAME)
        .master(MASTER)
        .getOrCreate()
    )

    print("Reading dataset...")

    df = spark.read.csv(
        RAW_DATA_PATH,
        header=True,
        inferSchema=True
    )

    print(f"Loaded {df.count()} records")

    features = create_features(df)

    print("Generated features")

    features.show(5, truncate=False)

    features.write.mode("overwrite").parquet(PROCESSED_DATA_PATH)

    print("Features saved successfully")

    spark.stop()


if __name__ == "__main__":
    main()