import os

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
    source_script_path = "%s/task.sh" % os.path.dirname(__file__)
    handler = "task"

    def execute(self, github_body):
        pass
