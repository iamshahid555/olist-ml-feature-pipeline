from confluent_kafka import Producer
import pandas as pd
import json

# Kafka configuration
conf = {
    "bootstrap.servers": "localhost:9092"
}

producer = Producer(conf)

TOPIC = "olist-orders"

# Load dataset
df = pd.read_csv("data/raw/olist_orders_dataset.csv")

print(f"Loaded {len(df)} records.")

# Send records to Kafka
for _, row in df.iterrows():
    producer.produce(
        TOPIC,
        json.dumps(row.to_dict()).encode("utf-8")
    )

producer.flush()

print(f"Successfully sent {len(df)} records to topic '{TOPIC}'.")