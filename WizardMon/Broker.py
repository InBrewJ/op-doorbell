import pika
import json
import time

RABBIT_HOST = "eggs.urawizard.com"
RABBIT_QUEUE = "q_WizardMon"
RABBIT_EXCHANGE = "e_WizardMon"


class Broker:
    def __init__(self):
        print("Broker module initialised...")

    def produce(self, message: str):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(RABBIT_HOST)
        )
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=RABBIT_EXCHANGE, exchange_type="fanout")
        self.channel.basic_publish(
            exchange=RABBIT_EXCHANGE, routing_key="", body=json.dumps(message)
        )
        self.connection.close()

    def __del__(self):
        self.connection.close()
