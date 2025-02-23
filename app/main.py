from fastapi import FastAPI
from app.consumers.kafka_consumer import start_kafka_consumer

app = FastAPI()

# Запуск Kafka consumer при старте приложения
@app.on_event("startup")
async def startup_event():
    start_kafka_consumer()