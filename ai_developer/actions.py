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
        "sandbox_action": "bold #E57B00",  # Adjust color as needed
    }
)

console = Console(theme=custom_theme)


def print_sandbox_action(action_type: str, action_message: str):
    console.print(
        f"[sandbox_action] [Sandbox Action][/sandbox_action] {action_type}: {action_message}"
    )


def save_content_to_file(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    path = args["path"]
    content = args["content"]
    mode = args.get("mode", "overwrite")  # Default mode is 'overwrite'
    # Used for 'insert' and 'modify_line' modes
    line_number = args.get("line_number", None)

    action_message = f"File path: {path}, Mode: {mode}"
    if line_number is not None:
        action_message += f", Line number: {line_number}"
    print_sandbox_action("Modifying file", action_message)

    try:
        _dir = os.path.dirname(path)
        sandbox.filesystem.make_dir(_dir)

        if mode == "overwrite":
            sandbox.filesystem.write(path, content)
        elif mode == "append":
            existing_content = sandbox.filesystem.read(path)
            new_content = existing_content + "\n" + content
            sandbox.filesystem.write(path, new_content)
        elif mode in ["insert", "modify_line"]:
            new_content = modify_or_insert_content(
                sandbox, path, content, line_number, mode
            )
            sandbox.filesystem.write(path, new_content)

        return "Success"
    except Exception as e:
        return f"Error: {e}"
def create_directory(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    _directory = args["path"]
    print_sandbox_action("Creating directory", _directory)

    try:
        sandbox.filesystem.make_dir(_directory)
        return "success"
    except Exception as e:
        return f"Error: {e}"


def save_content_to_file(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    path = args["path"]
    content = args["content"]
    mode = args.get("mode", "overwrite")  # Default mode is 'overwrite'
    # Used for 'insert' and 'modify_line' modes
    line_number = args.get("line_number", None)

    print_sandbox_action("Saving content to", path)

    try:
        _dir = os.path.dirname(path)
        sandbox.filesystem.make_dir(_dir)

        if mode == "overwrite":
            sandbox.filesystem.write(path, content)
        elif mode == "append":
            existing_content = sandbox.filesystem.read(path)
            new_content = existing_content + "\n" + content
            sandbox.filesystem.write(path, new_content)
        elif mode in ["insert", "modify_line"]:
            new_content = modify_or_insert_content(
                sandbox, path, content, line_number, mode
            )
            sandbox.filesystem.write(path, new_content)

        return "Success"
    except Exception as e:
        return f"Error: {e}"


def modify_or_insert_content(sandbox, path, content, line_number, mode):
    existing_content = sandbox.filesystem.read(path)
    lines = existing_content.split("\n")

    if mode == "insert":
        if line_number is not None and 0 <= line_number < len(lines):
            lines.insert(line_number, content)
        else:
            lines.append(content)
    elif mode == "modify_line":
        if line_number is not None and 0 <= line_number < len(lines):
            lines[line_number] = content

    return "\n".join(lines)


def list_files(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    path = args["path"]
    print_sandbox_action("Listing files on path", path)

    try:
        files = sandbox.filesystem.list(path)
        response = "\n".join(
            [f"dir: {file.name}" if file.is_dir else file.name for file in files]
        )
        return response
    except Exception as e:
        return f"Error: {e}"


def read_file(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    path = args["path"]
    print_sandbox_action("Reading file on path", path)

    try:
        return sandbox.filesystem.read(path)
    except Exception as e:
        return f"Error: {e}"


def commit(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    repo_directory = "/home/user/repo"
    commit_message = args["message"]
    print_sandbox_action("Committing with the message", commit_message)

    git_add_proc = sandbox.process.start_and_wait(f"git -C {repo_directory} add .")
    if git_add_proc.exit_code != 0:
        error = f"Error adding files to staging: {git_add_proc.stdout}\n\t{git_add_proc.stderr}"
        console.print("\t[bold red]Error:[/bold red]", error)
        return error

    git_commit_proc = sandbox.process.start_and_wait(
        f"git -C {repo_directory} commit -m '{commit_message}'"
    )
    if git_commit_proc.exit_code != 0:
        error = f"Error committing changes: {git_commit_proc.stdout}\n\t{git_commit_proc.stderr}"
        console.print("\t[bold red]Error:[/bold red]", error)
        return error

    return "success"


def make_pull_request(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    base_branch = "main"
    random_letters = "".join(random.choice(string.ascii_letters) for _ in range(5))
    new_branch_name = f"ai-developer-{random_letters}"

    title = args["title"]
    body = ""

    print_sandbox_action(
        "Making a pull request", f"from '{new_branch_name}' to '{base_branch}'"
    )

    git_checkout_proc = sandbox.process.start_and_wait(
        f"git -C {REPO_DIRECTORY} checkout -b {new_branch_name}"
    )
    if git_checkout_proc.exit_code != 0:
        error = f"Error creating a new git branch {new_branch_name}: {git_checkout_proc.stdout}\n\t{git_checkout_proc.stderr}"
        console.print("\t[bold red]Error:[/bold red]", error)
        return error

    git_push_proc = sandbox.process.start_and_wait(
        f"git -C {REPO_DIRECTORY} push -u origin {new_branch_name}"
    )
    if git_push_proc.exit_code != 0:
        error = (
            f"Error pushing changes: {git_push_proc.stdout}\n\t{git_push_proc.stderr}"
        )
        console.print("\t[bold red]Error:[/bold red]", error)
        return error

    gh_pull_request_proc = sandbox.process.start_and_wait(
        cmd=f'gh pr create --base "{base_branch}" --head "{new_branch_name}" --title "{title}" --body "{body}"'.replace(
            "`", "\\`"
        ),
        cwd=REPO_DIRECTORY,
    )
    if gh_pull_request_proc.exit_code != 0:
        error = f"Error creating pull request: {gh_pull_request_proc.stdout}\n\t{gh_pull_request_proc.stderr}"
        console.print("\t[bold red]Error:[/bold red]", error)
        return error

    return "success"


def git_pull(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    working_directory = args.get("working_directory", REPO_DIRECTORY)
    print_sandbox_action("Executing git pull in", working_directory)

    try:
        git_pull_proc = sandbox.process.start_and_wait(
            f"git -C {working_directory} pull"
        )
        if git_pull_proc.exit_code != 0:
            error = f"Error pulling changes: {git_pull_proc.stdout}\n\t{git_pull_proc.stderr}"
            console.print("\t[bold red]Error:[/bold red]", error)
            return error

        return "success"
    except Exception as e:
        return f"Error: {e}"

def git_reset(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    repo_directory = "/home/user/repo"
    working_branch = args.get("working_branch", "main")
    print_sandbox_action("Resetting repo to branch in origin", working_branch)

    try:
        # Fetch the latest changes from origin
        git_fetch_proc = sandbox.process.start_and_wait(f"git -C {repo_directory} fetch origin")
        if git_fetch_proc.exit_code != 0:
            error = f"Error fetching from origin: {git_fetch_proc.stdout}\n\t{git_fetch_proc.stderr}"
            console.print("\t[bold red]Error:[/bold red]", error)
            return error

        # Reset the local branch to match the origin branch
        git_reset_proc = sandbox.process.start_and_wait(f"git -C {repo_directory} reset --hard origin/{working_branch}")
        if git_reset_proc.exit_code != 0:
            error = f"Error resetting branch '{working_branch}': {git_reset_proc.stdout}\n\t{git_reset_proc.stderr}"
            console.print("\t[bold red]Error:[/bold red]", error)
            return error

        # Clean up any untracked files
        git_clean_proc = sandbox.process.start_and_wait(f"git -C {repo_directory} clean -fd")
        if git_clean_proc.exit_code != 0:
            error = f"Error cleaning untracked files: {git_clean_proc.stdout}\n\t{git_clean_proc.stderr}"
            console.print("\t[bold red]Error:[/bold red]", error)
            return error

        return "success"
    except Exception as e:
        return f"Error: {e}"

