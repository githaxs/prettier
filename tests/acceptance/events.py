import os

events = [{'pull_request': {'head': {'ref': 'GabeL7r-patch-9',
                                     'sha': '74ab2e085090cbf3d1edbf5b563468ab20ed1a6b'},
                            'commits': 392,
                            },
           'repository': {'full_name': 'githaxs/test'},
           'githaxs': {'token': os.getenv('GITHUB_TOKEN'),
                       'subscription_level': 5,
                       'task_settings': {},
                       'full_event_name': 'pull_request.opened'}}]
