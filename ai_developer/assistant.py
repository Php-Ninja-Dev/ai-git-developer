def rollback(to_commit: str):
    action = {
        'action': 'rollback',
        'to_commit': to_commit,
    }
    response = perform_sandbox_action(action)
    return response
