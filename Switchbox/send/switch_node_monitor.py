import serial
import time
from time import sleep
from serial import Serial
import json
import paho.mqtt.client as mqtt

DUMMY_MODE = False
SERIAL_CONN = '/dev/ttyACM0'
SERIAL_BAUD = 9600
SPEAKERBOX_PUB_TOPIC = 'switchbox/doorbell/trigger'
BROKER = 'speakerbox.local'
BROKER_PORT = 1883
HOPE_SERIAL_IS_OK_DELAY = 5
DING = 'ding'
DONG = 'dong'

## init serial

try:
    print("Initial serial connect attempt...")
    ser = Serial(SERIAL_CONN, baudrate=SERIAL_BAUD, timeout=None)
except:
    print("Could not connect to the serial line, activating DUMMY_MODE")
    DUMMY_MODE = True

## mqtt wrangling

def on_message(client, userdata, message):
    payload = str(message.payload.decode("utf-8"))
    print("message received " ,payload)
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True  # set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)
    
def ding():
    client.publish(SPEAKERBOX_PUB_TOPIC, DING)

def dong():
    client.publish(SPEAKERBOX_PUB_TOPIC, DONG)

def parse_message(message):
    message_dict = json.loads(message)
    ts = time.asctime( time.localtime(time.time()) )
    print(str(ts), ': message from serial: ', message)
    if (message_dict['message'] == DING):
        ding()
    if (message_dict['message'] == DONG):
        dong()

mqtt.Client.connected_flag = False  # create flag in class
client = mqtt.Client("Switchbox", clean_session=False)  # create new instance
client.on_connect = on_connect  # bind call back function
client.on_message = on_message #attach function to callback
client.loop_start()

print("Connecting to broker ", BROKER)
client.connect(BROKER, BROKER_PORT, 60)  # connect to broker

while not client.connected_flag:  # wait in loop
    print("In wait loop")
    sleep(1)

print("in Main Loop")
print("Listing to serial...")

# A hope-for-the-best sort of delay
sleep(HOPE_SERIAL_IS_OK_DELAY)

while(True):
    if not DUMMY_MODE:
        try:
            if(ser == None):
                ser = Serial(SERIAL_CONN, baudrate=SERIAL_BAUD, timeout=None)
                print("Reconnecting")

            line = ser.readline()   # read a '\n' terminated line
            decodedLine = line.decode('utf-8').rstrip()
            parse_message(decodedLine)
        except Exception as e:
            ts = time.asctime( time.localtime(time.time()) )
            print(str(ts), 'In main switchbox loop: ', e)
            if(not(ser == None)):
                ser.close()
                ser = None
                print("Disconnecting...")
            print("More than likely, no Connection or serial line borked")
            sleep(0.7)

client.loop_stop()  # Stop loop
client.disconnect()  # disconnect
