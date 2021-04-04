import json
import os

from code_check import CodeCheck
from task_interfaces import MetaTaskInterface


class Task(MetaTaskInterface):
    """
    Verifies files are formatted with prettier.
    """

    name = "Prettier"
    slug = "prettier"
    pass_summary = ""
    pass_text = ""
    fail_summary = "All files not formatted correctly."
    fail_text = ""
    actions = None

    def execute(self, github_body, settings) -> bool:
        code_check = CodeCheck(
            token=github_body.get("githaxs").get("token"),
            branch=github_body.get("pull_request", {}).get("head", {}).get("ref"),
            default_branch=github_body.get("repository", {}).get("default_branch"),
            full_repo_name=github_body.get("repository", {}).get("full_name"),
            source_script_path="%s/task.sh" % os.path.dirname(__file__),
            setting_files=[
                {
                    "file_name": ".prettierrc.json",
                    "contents": json.dumps(settings["prettier_config"]),
                }
            ],
        )

        code_check.execute()

        self.fail_text = code_check.fail_text

        return code_check.result
