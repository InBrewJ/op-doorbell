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
