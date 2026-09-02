import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

from .schema import OrderFeatures


DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql+psycopg://admin:admin123@localhost:5432/feature_store"
)

engine: Engine = create_engine(DATABASE_URL)


app = FastAPI(
    title="Olist ML Feature API",
    description="API for serving engineered Olist order features.",
    version="1.0.0",
)


class Health(BaseModel):
    status: str
    database: str


@app.get("/", tags=["General"])
def root():
    return {
        "message": "Olist ML Feature API is running"
    }


@app.get("/health", response_model=Health, tags=["General"])
def health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected"
        }

    except Exception:
        return {
            "status": "unhealthy",
            "database": "unavailable"
        }


@app.get(
    "/features/{order_id}",
    response_model=OrderFeatures,
    tags=["Features"]
)
def get_order_features(order_id: str):

    query = text(
        """
        SELECT
            order_id,
            customer_id,
            order_status,
            order_purchase_timestamp,
            order_approved_at,
            order_delivered_carrier_date,
            order_delivered_customer_date,
            order_estimated_delivery_date,
            delivery_time_days,
            carrier_delivery_days,
            delivery_delay_days,
            processing_time_days,
            purchase_year,
            purchase_month,
            purchase_day,
            purchase_weekday,
            is_delivered
        FROM orders_features
        WHERE order_id = :order_id
        """
    )

    try:
        with engine.connect() as connection:
            result = connection.execute(
                query,
                {"order_id": order_id}
            )

            row = result.mappings().first()

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {exc}"
        )

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Order features not found"
        )

    return dict(row)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000))
    )