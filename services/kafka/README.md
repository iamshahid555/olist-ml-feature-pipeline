# Kafka Service

## Purpose

This service ingests raw e-commerce transaction data from the Olist dataset into Apache Kafka.

## Responsibilities

- Read CSV data from `data/raw`
- Convert each record into JSON
- Publish messages to the Kafka topic `olist-orders`

## Technology

- Apache Kafka 7.7
- Python 3.11
- kafka-python