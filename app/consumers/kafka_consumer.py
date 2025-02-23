from confluent_kafka import Consumer, KafkaError
import json
from app.services.notification_service import handle_user_registered_event

def start_kafka_consumer():
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
            handle_user_registered_event(event)

    import threading
    threading.Thread(target=consume_messages, daemon=True).start()