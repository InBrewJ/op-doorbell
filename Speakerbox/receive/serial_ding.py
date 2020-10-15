from time import sleep
import paho.mqtt.client as mqtt
import mplayer

# Must start the broker via docker (or whatever) first!
BROKER = "localhost"
BROKER_PORT = 1883
SWITCHBOX_SUB_TOPIC = 'switchbox/doorbell/trigger'
SAMPLE_PATH = "../High-pitched-doorbell-ring-twice/High-pitched-doorbell-ring-twice.mp3"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True  # set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)

def on_message(client, userdata, message):
    payload = str(message.payload.decode("utf-8"))
    p.loadfile(SAMPLE_PATH)
    print("message received " ,payload)
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    mqtt2serial(payload, ser)


mqtt.Client.connected_flag = False  # create flag in class
client = mqtt.Client("Speakerbox")  # create new instance
client.on_connect = on_connect  # bind call back function
client.on_message = on_message #attach function to callback
client.loop_start()

print("Connecting to broker @ ", BROKER)
client.connect(BROKER, BROKER_PORT, 60)  # connect to broker

client.loop_forever()