HeartbeatSchema: dict = {
    'version': 1,
    'utc': None,
    'utc_pretty': None,
    'message': {
        'deviceId': None,
        'type': 'heartbeat'
    }
}

HookSchema: dict = {
    'version': 1,
    'utc': None,
    'utc_pretty': None,
    'message': {
        'deviceId': None,
        'errors': [],
        'event': {
            'type': None,
            'meta': None
        }
    },
}