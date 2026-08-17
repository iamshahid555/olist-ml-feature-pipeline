from pyspark.sql.functions import col


def clean_orders(df):
    """
    Clean and validate the orders dataset before feature engineering.
    """

    # Remove rows without a purchase timestamp
    df = df.filter(
        col("order_purchase_timestamp").isNotNull()
    )

    # Remove duplicate orders
    df = df.dropDuplicates(["order_id"])

    return df