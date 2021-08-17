import os
import json

from task_interfaces import SubscriptionLevels
from task_interfaces import TaskInterface
from task_interfaces import TaskTypes


class Task(TaskInterface):
    """
    Verifies files are formatted with prettier.
    """

    name = "Prettier"
    slug = "prettier"
    pass_summary = ""
    pass_text = ""
    fail_summary = "All files not formatted correctly."
    fail_text = ""
    subscription_level = SubscriptionLevels.FREE
    actions = None

    type = TaskTypes.CODE_FORMAT
    command = "prettier --write"
    file_filters = ".*.(js|ts|scss|css|yaml|yml|html|jsx)$"

    def execute(self, github_body):
        pass

    def pre_execute_hook(self, **kwargs):
        settings = kwargs['settings']

        if 'prettier_config' in settings:
            with open("/tmp/prettier_config.json", "w") as f:
                f.write(json.dumps(settings['prettier_config']))
            self.command += " --config /tmp/prettier_config.json"
