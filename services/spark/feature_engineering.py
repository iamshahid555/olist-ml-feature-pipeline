from pyspark.sql.functions import (
    col,
    datediff,
    when,
    year,
    month,
    dayofmonth,
    dayofweek
)


def add_delivery_features(df):
    """
    Creates delivery-related features.
    """

    df = df.withColumn(
        "delivery_time_days",
        datediff(
            col("order_delivered_customer_date"),
            col("order_purchase_timestamp")
        )
    )

    df = df.withColumn(
        "carrier_delivery_days",
        datediff(
            col("order_delivered_customer_date"),
            col("order_delivered_carrier_date")
        )
    )

    df = df.withColumn(
        "delivery_delay_days",
        datediff(
            col("order_delivered_customer_date"),
            col("order_estimated_delivery_date")
        )
    )

    return df


def add_processing_features(df):
    """
    Calculates the order approval time.
    """

    df = df.withColumn(
        "processing_time_days",
        datediff(
            col("order_approved_at"),
            col("order_purchase_timestamp")
        )
    )

    return df


def add_temporal_features(df):
    """
    Extracts useful calendar information.
    """

    df = df.withColumn(
        "purchase_year",
        year(col("order_purchase_timestamp"))
    )

    df = df.withColumn(
        "purchase_month",
        month(col("order_purchase_timestamp"))
    )

    df = df.withColumn(
        "purchase_day",
        dayofmonth(col("order_purchase_timestamp"))
    )

    df = df.withColumn(
        "purchase_weekday",
        dayofweek(col("order_purchase_timestamp"))
    )

    return df


def add_status_features(df):
    """
    Converts order status into a binary feature.
    """

    df = df.withColumn(
        "is_delivered",
        when(
            col("order_status") == "delivered",
            1
        ).otherwise(0)
    )

    return df


def create_features(df):

    df = add_delivery_features(df)

    df = add_processing_features(df)

    df = add_temporal_features(df)

    df = add_status_features(df)

    return df