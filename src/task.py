import json
import os

from task_interfaces import MetaTaskInterface
from task_interfaces import SubscriptionLevels


class Task(MetaTaskInterface):
    """
    Verifies files are formatted with prettier.
    """

    name = "Prettier"
    slug = "prettier"
    pass_summary = ""
    pass_text = ""
    fail_summary = "All files not formatted correctly."
    type = "code_format"
    source_script_path="%s/task.sh" % os.path.dirname(__file__)
    fail_text = ""
    _actions = [
        {"label": "Fix", "identifier": "fix", "description": "Fix formatting issues."}
    ]
    subscription_level = SubscriptionLevels.FREE

    def execute(self):
        pass
    
    @property
    def actions(self):
        return self._actions

    @actions.setter
    def actions(self, actions):
        self._actions = actions
