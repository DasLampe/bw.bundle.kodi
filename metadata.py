@metadata_reactor
def add_user(metadata):
    if not node.has_bundle('users'):
        raise DoNotRunAgain

    return {
        'users': {
            'kodi': {
                'fullname': 'Kodi User',
                'add_groups': ["audio", "video", "input", "dialout", "plugdev", "tty"],
                'shell': '/bin/sh',
            }
        }
    }

@metadata_reactor
def add_pkg_apt(metadata):
    if not node.has_bundle('apt'):
        raise DoNotRunAgain

    return {
        'apt': {
            'packages': {
                'kodi': {'installed': True},
            },
        },
    }
