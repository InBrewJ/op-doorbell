from time import sleep
import paho.mqtt.client as mqtt
import mplayer

# Must start the broker via docker (or whatever) first!
BROKER = "localhost"
BROKER_PORT = 1883
SWITCHBOX_SUB_TOPIC = 'switchbox/doorbell/trigger'
SAMPLE_PATH = "../High-pitched-doorbell-ring-twice/High-pitched-doorbell-ring-twice.mp3"
audio_player = None

def init_audio():
    jack = 0.0
    return mplayer.Player(args=['-ao', 'alsa:device=hw='+str(jack)])

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True  # set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)

def on_message(client, userdata, message):
    payload = str(message.payload.decode("utf-8"))
    audio_player.loadfile(SAMPLE_PATH)
    print("message received " ,payload)
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

audio_player = init_audio()
sleep(5)
mqtt.Client.connected_flag = False  # create flag in class

client = mqtt.Client("Speakerbox", clean_session=False)  # create new instance
client.on_connect = on_connect  # bind call back function
client.on_message = on_message #attach function to callback
client.loop_start()

print("Connecting to broker @ ", BROKER)
client.connect(BROKER, BROKER_PORT, 60)  # connect to broker

while not client.connected_flag:  # wait in loop
    print("In wait loop")
    sleep(1)

print("Subscribing to topic", SWITCHBOX_SUB_TOPIC)
client.subscribe(SWITCHBOX_SUB_TOPIC)
print("Paho: looping forever...")

def send_heartbeat():
    print('Heartbeat')

while(True):
    sleep(1)
    send_heartbeat()

client.loop_stop()  # Stop loop
client.disconnect()  # disconnect