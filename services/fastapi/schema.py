from datetime import datetime

from pydantic import BaseModel


class OrderFeatures(BaseModel):
    order_id: str
    customer_id: str
    order_status: str

    order_purchase_timestamp: datetime
    order_approved_at: datetime | None = None
    order_delivered_carrier_date: datetime | None = None
    order_delivered_customer_date: datetime | None = None
    order_estimated_delivery_date: datetime | None = None

    delivery_time_days: int | None = None
    carrier_delivery_days: int | None = None
    delivery_delay_days: int | None = None
    processing_time_days: int | None = None

    purchase_year: int | None = None
    purchase_month: int | None = None
    purchase_day: int | None = None
    purchase_weekday: int | None = None

    is_delivered: int