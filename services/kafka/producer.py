from confluent_kafka import Producer
import json

conf = {
    "bootstrap.servers": "localhost:9092"
}

producer = Producer(conf)

print("Successfully connected to Kafka!")

producer.flush()