# Switchbox

aka the Pine64 running DietPi with the Arduino plugged into it

## Useful commands

- ssh into directory:

```
ssh -t root@switchbox.local "cd ~/workshop ; bash"
```

- Send updated code from host to speakerbox:

```
scp <code>
ssh user@speakerbox.local 'stop_old_version && run_new_version && run_tests'
```

Automatically connect to WiFi:

- See etc_network_interfaces

Monitor box_check with:

- Potential startup script:

```
# Run cron as root
sudo crontab -e
# Add line:
@reboot sleep 10 && /usr/bin/python3 -u /root/workshop/send/switch_node_monitor.py >> /root/workshop/switchbox.log 2>&1 &
```
