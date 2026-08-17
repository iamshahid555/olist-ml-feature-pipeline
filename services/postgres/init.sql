CREATE TABLE IF NOT EXISTS orders_features (

    order_id VARCHAR(100) PRIMARY KEY,

    customer_id VARCHAR(100),

    order_status VARCHAR(30),

    order_purchase_timestamp TIMESTAMP,

    delivery_time_days INTEGER,

    processing_time_days INTEGER,

    carrier_delivery_days INTEGER,

    delivery_delay_days INTEGER,

    purchase_year INTEGER,

    purchase_month INTEGER,

    purchase_day INTEGER,

    purchase_weekday INTEGER,

    is_delivered INTEGER

);