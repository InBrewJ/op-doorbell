from WizardMon import WizardMon

wm = WizardMon('Speakerbox')
wm.heartbeat()
event = {
    'type': 'dong',
    'meta': ''
}
wm.hook(event)