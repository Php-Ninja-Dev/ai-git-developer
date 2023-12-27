

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
