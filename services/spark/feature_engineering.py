from pyspark.sql.functions import col, datediff


def create_features(df):
    """
    Creates engineered features from the orders dataset.
    """

    df = df.withColumn(
        "delivery_time_days",
        datediff(
            col("order_delivered_customer_date"),
            col("order_purchase_timestamp")
        )
    )

    return df