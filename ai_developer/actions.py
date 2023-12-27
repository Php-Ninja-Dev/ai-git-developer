
def cherrypick(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    commit_hash = args["commit_hash"]
    print_sandbox_action("Cherry-picking commit", commit_hash)

    try:
        cherrypick_proc = sandbox.process.start_and_wait(
            f"git -C {REPO_DIRECTORY} cherry-pick {commit_hash}"
        )
        if cherrypick_proc.exit_code != 0:
            error = f"Error cherry-picking commit: {cherrypick_proc.stdout}\n\t{cherrypick_proc.stderr}"
            console.print("\t[bold red]Error:[/bold red]", error)
            return error

        return "success"
    except Exception as e:
        return f"Error: {e}"


def rollback(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    commit_hash = args["commit_hash"]
    print_sandbox_action("Rolling back to commit", commit_hash)

    try:
        reset_proc = sandbox.process.start_and_wait(
            f"git -C {REPO_DIRECTORY} reset --hard {commit_hash}"
        )
        if reset_proc.exit_code != 0:
            error = f"Error rolling back to commit: {reset_proc.stdout}\n\t{reset_proc.stderr}"
            console.print("\t[bold red]Error:[/bold red]", error)
            return error

        return "success"
    except Exception as e:
        return f"Error: {e}"