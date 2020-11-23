import pika
import json
import time

ts: str = str(time.asctime( time.localtime(time.time()) ))
message: dict = {
    'version': 1,
    'timestamp': ts,
    'message': 'heartbeater',
    'status': {
        'ding': True,
        'dong': False
    }
}
RABBIT_HOST= 'eggs.urawizard.com'

connection = pika.BlockingConnection(pika.ConnectionParameters(RABBIT_HOST))
channel = connection.channel()

channel.queue_declare(queue='t_wizard_mon')

channel.basic_publish(exchange='',
                      routing_key='t_wizard_mon',
                      body=json.dumps(message))
print(f" [x] Sent {message}")

connection.close()