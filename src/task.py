import os

from task_interfaces import TaskInterface, SubscriptionLevels, TaskTypes


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
