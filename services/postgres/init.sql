CREATE TABLE IF NOT EXISTS customer_features (
    customer_id VARCHAR(100) PRIMARY KEY,
    total_orders INTEGER,
    average_order_value DECIMAL(10,2),
    last_order_date TIMESTAMP
);