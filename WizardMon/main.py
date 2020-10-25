from WizardMon import WizardMon

wm = WizardMon('Speakerbox')
wm.heartbeat(meta='extra')
event = {
    'type': 'dong',
    'meta': ''
}
wm.hook('dong', 'something')