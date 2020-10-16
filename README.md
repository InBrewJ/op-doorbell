# op-doorbell

## Helpful things

Remember, if you're doing to install the open ssh agent then root login isn't enabled by default!

- https://serverpilot.io/docs/how-to-enable-ssh-password-authentication/
  (scp wouldn't work with the dietpi and then I couldn't log in via the root user)
- enable password auth
- enable root login

## Helpful commands

Watch your own 192.x.x.x IPs:

```
watch -n 1 'ip a | grep inet | grep 192'
```
