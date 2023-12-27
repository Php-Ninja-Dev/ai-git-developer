def rollback(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    repo_directory = "/home/user/repo"
    to_commit = args["to_commit"]
    print_sandbox_action("Rolling back to commit", to_commit)

    git_reset_proc = sandbox.process.start_and_wait(f"git -C {repo_directory} reset --hard {to_commit}")
    if git_reset_proc.exit_code != 0:
        error = f"Error resetting to commit {to_commit}: {git_reset_proc.stdout}\n\t{git_reset_proc.stderr}"
        console.print("\t[bold red]Error:[/bold red]", error)
        return error

    return "success"
