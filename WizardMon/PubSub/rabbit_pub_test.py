#!/usr/bin/env python3
import pika
import sys
import time

ts: str = str(time.asctime(time.localtime(time.time())))

HOST = "eggs.urawizard.com"
RABBIT_EXCHANGE = "e_WizardMon"

connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
channel = connection.channel()

channel.exchange_declare(exchange=RABBIT_EXCHANGE, exchange_type="fanout")

message = " ".join(sys.argv[1:]) or ts + " :: info: Hello World!"
channel.basic_publish(exchange=RABBIT_EXCHANGE, routing_key="", body=message)
print(" [x] Sent %r" % message)
connection.close()