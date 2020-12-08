import pika
import json
import time

RABBIT_HOST = "eggs.urawizard.com"
RABBIT_QUEUE = "t_wizard_mon"


class Broker:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(RABBIT_HOST)
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=RABBIT_QUEUE)

    def produce(self, message: str):
        self.channel.basic_publish(
            exchange="", routing_key="t_wizard_mon", body=json.dumps(message)
        )

    def __del__(self):
        self.connection.close()
