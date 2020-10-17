# Speakerbox

aka the Raspberry Pi 3B+ with the usb speakers plugged into it

## Useful commands

- ssh into directory:

```
ssh -t pi@speakerbox.local "cd ~/workshop ; bash"
```

- Send updated code from host to speakerbox:

```
scp -r ./* pi@speakerbox.local:workshop
ssh user@speakerbox.local 'stop_old_version && run_new_version && run_tests'
```

- Potential startup script:

```
# Run cron as regular user (docker group must be added to user!)
crontab -e
# Add lines:
@reboot /usr/local/bin/docker-compose -f /home/pi/workshop/infra/docker-compose.yaml up -d && /usr/bin/python3 -u /home/pi/workshop/receive/switchbox_monitor.py >> /home/pi/workshop/speakerbox.log 2>&1 &
```
