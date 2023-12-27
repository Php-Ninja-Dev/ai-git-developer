import os
import random
import string
from typing import Any, Dict
from e2b import Sandbox
from rich.console import Console
from rich.theme import Theme
import ftplib

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
        return "success"
    except Exception as e:
        return f"Error: {e}"


def save_content_to_file(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    path = args["path"]
    content = args["content"]
    print_sandbox_action("Saving content to", path)

    try:
        dir = os.path.dirname(path)
        sandbox.filesystem.make_dir(dir)
        sandbox.filesystem.write(path, content)
        return "success"
    except Exception as e:
        return f"Error: {e}"


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
def save_content_to_file(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    path = args["path"]
    content = args["content"]
    append = args.get("append", True)
    print_sandbox_action("Saving content", f'to {path}, append: {append}')
    mode = 'a' if append else 'w'

    try:
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
            sandbox.filesystem.make_dir(dir)
        if not append and os.path.exists(path):
            confirmation = args.get('confirmation', False)
            if not confirmation:
                return "Error: File exists, and overwrite confirmation not provided."
        sandbox.filesystem.write(path, content, mode=mode)
        return "success"
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
def save_content_to_file(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    path = args["path"]
    content = args["content"]
    append = args.get("append", False)
    overwrite = args.get("overwrite", False)
    print_sandbox_action("Saving content", f'to {path}, append: {append}')
    mode = 'a' if append else 'w'

    # Check if overwrite is True or if the file doesn't exist, then write the content.
    if overwrite or not os.path.exists(path):
        try:
            dir = os.path.dirname(path)
            if not os.path.exists(dir):
                sandbox.filesystem.make_dir(dir)
            sandbox.filesystem.write(path, content, mode=mode)
            return "success"
        except Exception as e:
            return f"Error: {e}"
    else:
        return "Error: File exists and overwrite is set to False."

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
            "`", "\`"
        ),
        cwd=REPO_DIRECTORY,
    )
    if gh_pull_request_proc.exit_code != 0:
        error = f"Error creating pull request: {gh_pull_request_proc.stdout}\n\t{gh_pull_request_proc.stderr}"
        console.print("\t[bold red]Error:[/bold red]", error)
        return error

    return "success"


def modify_file_line(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    path = args["path"]
    line_number = args["line_number"]
    new_content = args.get("new_content", None)
    action = args.get("action", "replace")
    print_sandbox_action("Modifying file line", f'path: {path}, line: {line_number}, action: {action}')

    try:
        file_content = sandbox.filesystem.read(path)
        file_lines = file_content.split('\n')
        if action == "insert_above":
            file_lines.insert(line_number - 1, new_content)
        elif action == "insert_below":
            file_lines.insert(line_number, new_content)
        elif action == "replace":
            file_lines[line_number - 1] = new_content
        else:
            return f"Error: Unsupported action '{action}'"

        updated_content = '\n'.join(file_lines)
        sandbox.filesystem.write(path, updated_content)
        return "success"
    except Exception as e:
        console.print(f"Error: ",e)
        return f"Error: {e}"

def send_email(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    recipients = args["recipients"]
    subject = args["subject"]
    body = args["body"]
    print_sandbox_action("Sending email to", ', '.join(recipients))


def delete_file(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    # Deletes a file from the sandbox's file system
    # Args:
    #     sandbox: The sandbox instance
    #     args: A dictionary containing the path of the file to delete under the key 'path'
    path = args['path']
    print_sandbox_action('Deleting file', path)

    try:
        sandbox.filesystem.remove(path)
        return 'success'
    except Exception as e:
        return f"Error: {e}"


def copy_file(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    # Copies a file within the sandbox's file system
    # Args:
    #     sandbox: The sandbox instance
    #     args: A dictionary containing:
    #           'src_path': The source path of the file to copy
    #           'dest_path': The destination path of the file
    print_sandbox_action('Copying file', f"{args['src_path']} to {args['dest_path']}")

    try:
        sandbox.filesystem.copy(args['src_path'], args['dest_path'])
        return 'success'
    except Exception as e:
        return f"Error: {e}"


def rename_file(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    # Renames a file within the sandbox's file system
    # Args:
    #     sandbox: The sandbox instance
    #     args: A dictionary containing:
    #           'old_path': The current path of the file
    #           'new_path': The new path (including new file name) of the file
    old_path = args['old_path']
    new_path = args['new_path']
    print_sandbox_action('Renaming file', f"{old_path} to {new_path}")

    try:
        sandbox.filesystem.rename(old_path, new_path)
        return 'success'
    except Exception as e:
        return f"Error: {e}"


def find_replace_in_file(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    # Finds and replaces text within a file in the sandbox's file system
    # Args:
    #     sandbox: The sandbox instance
    #     args: A dictionary containing:
    #           'path': The path of the file
    #           'find': The text to find
    #           'replace': The text to replace it with
    path = args['path']
    find_text = args['find']
    replace_text = args['replace']
    print_sandbox_action('Finding and replacing in file', f"{path}")

    try:
        file_content = sandbox.filesystem.read(path)
        updated_content = file_content.replace(find_text, replace_text)
        sandbox.filesystem.write(path, updated_content)
        return 'success'
    except Exception as e:
        return f"Error: {e}"


def check_git_status(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    # Checks the git status of the repo
    # Args:
    #     sandbox: The sandbox instance
    #     args: A dictionary with no specific keys needed
    repo_directory = '/home/user/repo'
    print_sandbox_action('Checking git status of', repo_directory)

    try:
        git_status_proc = sandbox.process.start_and_wait(f'git -C {repo_directory} status')
        if git_status_proc.exit_code != 0:
            error = f"Error checking git status: {git_status_proc.stdout}\n\t{git_status_proc.stderr}"
            console.print('\t[bold red]Error:[/bold red]', error)
            return error
        return git_status_proc.stdout
    except Exception as e:
        return f"Error: {e}"


def git_pull(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    # Pulls the latest changes from the git repository
    # Args:
    #     sandbox: The sandbox instance
    #     args: A dictionary with no specific keys needed
    repo_directory = '/home/user/repo'
    branch = args.get('branch', 'main')  # Defaults to the main branch if not specified
    print_sandbox_action('Pulling the latest changes from', branch)

    try:
        git_pull_proc = sandbox.process.start_and_wait(f'git -C {repo_directory} pull origin {branch}')
        if git_pull_proc.exit_code != 0:
            error = f"Error pulling changes from {branch}: {git_pull_proc.stdout}\n\t{git_pull_proc.stderr}"
            console.print('\t[bold red]Error:[/bold red]', error)
            return error
        return 'success'
    except Exception as e:
        return f"Error: {e}"


def download_ftp_folder(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    ftp_server = args['ftp_server']
    ftp_path = args['ftp_path']
    local_path = args['local_path']
    username = args.get('username')
    password = args.get('password')

    print_sandbox_action('Downloading FTP folder', f"{ftp_path} to {local_path}")

    try:
        with ftplib.FTP(ftp_server) as ftp:
            if username and password:
                ftp.login(username, password)
            else:
                ftp.login()

            filenames = ftp.nlst(ftp_path)
            sandbox.filesystem.make_dir(local_path)

            for filename in filenames:
                local_filepath = os.path.join(local_path, os.path.basename(filename))
                with open(local_filepath, 'wb') as f:
                    ftp.retrbinary('RETR ' + filename, f.write)

        return 'success'
    except ftplib.all_errors as e:
        return f"FTP error: {e}"
    except Exception as e:
        return f"Error: {e}"