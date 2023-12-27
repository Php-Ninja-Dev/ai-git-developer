

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


def pull_latest_changes(sandbox: Sandbox, args: Dict[str, Any]) -> str:
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
