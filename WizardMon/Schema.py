HeartbeatSchema: dict = {
    'version': 1,
    'utc': None,
    'utc_pretty': None,
    'message': {
        'deviceId': None,
        'type': 'heartbeat',
        'meta': None
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