import os

events = [{'pull_request': {'head': {'ref': 'demo',
                                     'sha': 'e58df099cff2fa1d0df02dff67ae01260705fcf8'},
                            'commits': 3,
                            },
           'repository': {'full_name': 'githaxs/demo'},
           'githaxs': {'token': os.getenv('GITHUB_TOKEN'),
                       'subscription_level': 5,
                       'task_settings': {"prettier_config": "@azz/prettier-config"},
                       'full_event_name': 'pull_request.opened'}}]
