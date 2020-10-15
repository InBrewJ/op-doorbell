# Speakerbox

aka the Raspberry Pi 3B+ with the usb speakers plugged into it

## Useful commands

- ssh into directory:

```
ssh -t pi@speakerbox.local "cd ~/workshop ; bash"
```

- Send updated code from host to speakerbox:

```
scp <code>
ssh user@speakerbox.local 'stop_old_version && run_new_version && run_tests'
```
