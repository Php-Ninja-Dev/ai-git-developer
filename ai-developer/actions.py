

def rollback(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    commit_ref = args['commit_ref']
    print_sandbox_action('Rolling back to commit', commit_ref)

    git_reset_proc = sandbox.process.start_and_wait(f"git -C {REPO_DIRECTORY} reset --hard {commit_ref}")
    if git_reset_proc.exit_code != 0:
        error = f"Error during rollback to {commit_ref}: {git_reset_proc.stdout}\n\t{git_reset_proc.stderr}"
        console.print("\t[bold red]Error:[/bold red]", error)
        return error

    return 'success'


def reset(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    commit_ref = args['commit_ref']
    hard = args.get('hard', False)
    print_sandbox_action('Resetting to commit', commit_ref)

    reset_mode = '--hard' if hard else '--soft'
    git_reset_proc = sandbox.process.start_and_wait(f"git -C {REPO_DIRECTORY} reset {reset_mode} {commit_ref}")
    if git_reset_proc.exit_code != 0:
        error = f"Error during reset to {commit_ref}: {git_reset_proc.stdout}\n\t{git_reset_proc.stderr}"
        console.print("\t[bold red]Error:[/bold red]", error)
        return error

    return 'success'


def cherrypick(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    commit_ref = args['commit_ref']
    print_sandbox_action('Cherry-picking commit', commit_ref)

    git_cherry_pick_proc = sandbox.process.start_and_wait(f"git -C {REPO_DIRECTORY} cherry-pick {commit_ref}")
    if git_cherry_pick_proc.exit_code != 0:
        error = f"Error during cherry-pick of {commit_ref}: {git_cherry_pick_proc.stdout}\n\t{git_cherry_pick_proc.stderr}"
        console.print("\t[bold red]Error:[/bold red]", error)
        return error

    return 'success'
