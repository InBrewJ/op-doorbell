import pika

message = 'Heartbeat 0 status 1'

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='t_wizard_mon')

channel.basic_publish(exchange='',
                      routing_key='t_wizard_mon',
                      body=message)
print(f" [x] Sent {message}")

connection.close()