#!/usr/bin/env python3
import pika
import sys
import time

ts: str = str(time.asctime(time.localtime(time.time())))

HOST = "eggs.urawizard.com"

connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
channel = connection.channel()

channel.exchange_declare(exchange="logs", exchange_type="fanout")

message = " ".join(sys.argv[1:]) or ts + " :: info: Hello World!"
channel.basic_publish(exchange="logs", routing_key="", body=message)
print(" [x] Sent %r" % message)
connection.close()