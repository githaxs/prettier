import os

from task_interfaces import SubscriptionLevels
from task_interfaces import FormatTask
from task_interfaces import TaskTypes


class Task(FormatTask):
    """
    Verifies files are formatted with prettier.
    """

    name = "Prettier"
    subscription_level = SubscriptionLevels.STARTUP
    source_script_path = "%s/task.sh" % os.path.dirname(__file__)
