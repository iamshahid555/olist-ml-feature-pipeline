from config import (
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_DATABASE,
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_TABLE,
)


def write_to_postgres(df):
    """
    Writes the engineered features to PostgreSQL.
    """

    jdbc_url = (
        f"jdbc:postgresql://{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"
    )

    properties = {
        "user": POSTGRES_USER,
        "password": POSTGRES_PASSWORD,
        "driver": "org.postgresql.Driver",
    }

    (
        df.write
        .mode("overwrite")
        .jdbc(
            url=jdbc_url,
            table=POSTGRES_TABLE,
            properties=properties,
        )
    )

    print(f"Successfully wrote data to '{POSTGRES_TABLE}'.")