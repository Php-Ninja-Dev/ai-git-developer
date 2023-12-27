import os
import random
import string
from typing import Any, Dict
from e2b import Sandbox
from rich.console import Console
from rich.theme import Theme

REPO_DIRECTORY = "/home/user/repo"

custom_theme = Theme(
    {
        "sandbox_action": "bold #E57B00",
    }
)

console = Console(theme=custom_theme)


def print_sandbox_action(action_type: str, action_message: str):
    console.print(
        f"[sandbox_action] [Sandbox Action][/sandbox_action] {action_type}: {action_message}"
    )


# List of actions for the assistant
def create_directory(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    directory = args["path"]
    print_sandbox_action("Creating directory", directory)

    try:
        sandbox.filesystem.make_dir(directory)
    [... truncated] How to rollback the active branch to a specific commit.

    :param repo_path: The path to the git repository.
    :param commit_hash: The hash of the commit to rollback to.
    :return: Output of the rollback operation.
    """
    # TODO: Write the rollback function code here
    pass
