if not node.has_bundle('apt'):
    pkg_apt = {
        'kodi': {
            'installed': True
        },
    }

if node.metadata.get('kodi', {}).get('autostart', True):
    files = {
        '/etc/systemd/system/kodi.service': {
            'source': 'kodi.service',
            'owner': 'root',
            'group': 'root',
        }
    }

    svc_systemd = {
        'kodi.service': {
            'enabled': True,
            'running': True,
            'needs': {
                'file:/etc/systemd/system/kodi.service',
                'pkg_apt:kodi',
            }
        }
    }

