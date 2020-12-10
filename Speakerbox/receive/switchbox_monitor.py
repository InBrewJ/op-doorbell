from time import sleep
import paho.mqtt.client as mqtt
import mplayer
import time
import subprocess
from subprocess import Popen, PIPE
from shlex import split
import sys

sys.path.insert(1, "/home/pi/workshop/WizardMon")
from WizardMon import WizardMon

import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

logging.info("Starting up...")

# Must start the mosquitto broker via docker (or however) first!
BROKER = "localhost"
BROKER_PORT = 1883
SWITCHBOX_SUB_TOPIC = "switchbox/doorbell/trigger"
SAMPLE_PATH = "/home/pi/workshop/High-pitched-doorbell-ring-twice/High-pitched-doorbell-ring-twice.mp3"
audio_player = None
JACK = 0.0
VOLUME_QUERY_SOURCE = "amixer"
VOLUME_QUERY_SED = "sed -n '/Headphone/,/Mono:/p'"
VOLUME_QUERY_GREP = "grep -oP '\[.*?\]'"
wm = WizardMon("Speakerbox")


def get_headphone_volume_as_array():
    p1 = Popen(VOLUME_QUERY_SOURCE, stdout=PIPE)
    p2 = Popen(split(VOLUME_QUERY_SED), stdin=p1.stdout, stdout=PIPE)
    p3 = Popen(
        split(VOLUME_QUERY_GREP), stdin=p2.stdout, stdout=subprocess.PIPE, text=True
    )
    stdout, stderr = p3.communicate()
    return stdout.split("\n")


def get_headphone_volume_stats() -> dict:
    stats_as_array = get_headphone_volume_as_array()[:3]
    mapping = ["volume_percent", "volume_db", "speakersAre"]
    stats_dict = {}
    for idx, stat in enumerate(stats_as_array):
        without_brackets = stat.strip("[").strip("]")
        stats_dict[mapping[idx]] = without_brackets
    return stats_dict


def init_audio():
    return mplayer.Player(args=["-ao", "alsa:device=hw=" + str(JACK)])


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True  # set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def handle_message(message: dict):
    if message == "dong":
        _localtime = time.asctime(time.localtime(time.time()))
        print(_localtime, " *********** audio trigger via dong ***********")
        audio_player.loadfile(SAMPLE_PATH)


def on_message(client, userdata, message):
    payload = str(message.payload.decode("utf-8"))
    handle_message(payload)
    wm.hook(eventType=payload, eventMeta="after handle_message call!")
    print("message received ", payload)
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)


audio_player = init_audio()
sleep(5)
mqtt.Client.connected_flag = False  # create flag in class

client = mqtt.Client("Speakerbox", clean_session=False)  # create new instance
client.on_connect = on_connect  # bind call back function
client.on_message = on_message  # attach function to callback
client.loop_start()
logging.info("Paho: looping forever...")

print("Connecting to broker @ ", BROKER)
client.connect(BROKER, BROKER_PORT, 60)  # connect to broker

while not client.connected_flag:  # wait in loop
    print("In wait loop")
    sleep(1)

logging.info("Subscribing to topic: " + SWITCHBOX_SUB_TOPIC)
client.subscribe(SWITCHBOX_SUB_TOPIC)


def send_heartbeat():
    localtime = time.asctime(time.localtime(time.time()))
    try:
        wm.heartbeat(meta=get_headphone_volume_stats())
    except Exception as e:
        print("Could not send heartbeat: ", e)


logging.info("Just before main loop...")

while True:
    sleep(5)
    send_heartbeat()

client.loop_stop()  # Stop loop
client.disconnect()  # disconnect