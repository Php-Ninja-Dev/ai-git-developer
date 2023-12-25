

def rollback(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    repo_directory = "/home/user/repo"
    commit_hash = args["commit_hash"]
    print_sandbox_action("Rolling back to", commit_hash)

    git_reset_proc = sandbox.process.start_and_wait(f"git -C {repo_directory} reset --hard {commit_hash}")
    if git_reset_proc.exit_code != 0:
        error = f"Error during git reset: {git_reset_proc.stdout}\n\t{git_reset_proc.stderr}"
        console.print("\t[bold red]Error:[/bold red]", error)
        return error

    return "success"


def reset(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    repo_directory = "/home/user/repo"
    mode = args.get("mode", "--soft")
    commit_hash = args["commit_hash"]
    print_sandbox_action("Resetting repository with mode", mode)

    git_reset_proc = sandbox.process.start_and_wait(f"git -C {repo_directory} reset {mode} {commit_hash}")
    if git_reset_proc.exit_code != 0:
        error = f"Error during git reset: {git_reset_proc.stdout}\n\t{git_reset_proc.stderr}"
        console.print("\t[bold red]Error:[/bold red]", error)
        return error

    return "success"


def cherry_pick(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    repo_directory = "/home/user/repo"
    commit_hashes = args["commit_hashes"]
    print_sandbox_action("Cherry-picking commits", ", ".join(commit_hashes))

    for commit_hash in commit_hashes:
        git_cherry_pick_proc = sandbox.process.start_and_wait(f"git -C {repo_directory} cherry-pick {commit_hash}")
        if git_cherry_pick_proc.exit_code != 0:
            error = f"Error during git cherry-pick: {git_cherry_pick_proc.stdout}\n\t{git_cherry_pick_proc.stderr}"
            console.print("\t[bold red]Error:[/bold red]", error)
            return error

    return "success"