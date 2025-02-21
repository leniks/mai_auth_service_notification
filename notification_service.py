from fastapi import FastAPI
from confluent_kafka import Consumer, KafkaError
import json
import threading

app = FastAPI()

# Конфигурация Kafka Consumer
conf = {
    'bootstrap.servers': 'host.docker.internal:9093',
    'group.id': 'notification_group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
consumer.subscribe(['user_events'])

def consume_messages():
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(f"Error: {msg.error()}")
                break

        event = json.loads(msg.value().decode('utf-8'))
        print(f"Received event: {event}")
        # Обработать событие (например, отправить письмо)
        if event['eventType'] == 'UserRegistered':
            print(f"Sending welcome email to {event['email']}")

# Запуск потребителя в отдельном потоке
threading.Thread(target=consume_messages, daemon=True).start()

@app.get("/health")
async def health():
    return {"status": "ok"}