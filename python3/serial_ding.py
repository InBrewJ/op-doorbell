import serial
from time import sleep
from serial import Serial
import mplayer
import json

DUMMY_MODE = False
SERIAL_CONN = '/dev/ttyACM0'
SERIAL_BAUD = 9600
SAMPLE_PATH = "../High-pitched-doorbell-ring-twice/High-pitched-doorbell-ring-twice.mp3"

try:
    ser = Serial(SERIAL_CONN, baudrate=SERIAL_BAUD, timeout=None)
except:
    print("Could not connect to the serial line, activating DUMMY_MODE")
    DUMMY_MODE = True

def on_message(client, userdata, message):
    payload = str(message.payload.decode("utf-8"))
    print("message received " ,payload)
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    mqtt2serial(payload, ser)

def parse_message(message):
    message_dict = json.loads(message)
    if (message_dict['message'] == 'ding'):
        p.loadfile(SAMPLE_PATH)


p = mplayer.Player()

while(True):
    if not DUMMY_MODE:
        line = ser.readline()   # read a '\n' terminated line
        try:
            decodedLine = line.decode('utf-8').rstrip()
            parse_message(decodedLine)
        except Exception as e:
            print('Serial is a bit janky, retrying...', e)
            sleep(0.5)
