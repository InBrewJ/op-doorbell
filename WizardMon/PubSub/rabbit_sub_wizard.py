#!/usr/bin/env python3
import pika

HOST = "eggs.urawizard.com"
RABBIT_EXCHANGE = "e_WizardMon"

connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
channel = connection.channel()

channel.exchange_declare(exchange=RABBIT_EXCHANGE, exchange_type="fanout")

result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange=RABBIT_EXCHANGE, queue=queue_name)

print(" [*] Waiting for logs. To exit press CTRL+C")


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()