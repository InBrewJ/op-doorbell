import pika
import json
import time
from datetime import timezone 
import datetime 
from Schema import HeartbeatSchema, HookSchema
from Broker import Broker

class WizardMon:
    def __init__(self, deviceId):
        self.deviceId = deviceId
        self.broker = Broker()
        print('Init-ed')

    def _get_timestamp_utc(self):
        dt = datetime.datetime.now() 
        utc_time = dt.replace(tzinfo = timezone.utc) 
        utc_timestamp:str = str(utc_time.timestamp()) 
        return (utc_timestamp, str(utc_time))
    
    def heartbeat(self, meta: dict = {}):
        print('Sending hearbeat to broker')
        msg = HeartbeatSchema.copy()
        (utc, utc_pretty) = self._get_timestamp_utc()
        msg['utc'] = utc
        msg['utc_pretty'] = utc_pretty
        msg['message']['deviceId'] = self.deviceId
        msg['message']['meta'] = meta
        to_send: str = json.dumps(msg)
        self.broker.produce(to_send)

    def hook(self, eventType, eventMeta, errors = []):
        print('Sending hook to broker')
        msg = HookSchema.copy()
        (utc, utc_pretty) = self._get_timestamp_utc()
        msg['utc'] = utc
        msg['utc_pretty'] = utc_pretty
        msg['message']['deviceId'] = self.deviceId
        msg['message']['errors'] = errors
        msg['message']['event']['type'] = eventType
        msg['message']['event']['meta'] = eventMeta
        to_send: str = json.dumps(msg)
        self.broker.produce(to_send)
