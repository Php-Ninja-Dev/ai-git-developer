def save_content_to_file(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    path = args['path']
    content = args['content']
    print_sandbox_action('Saving content to', path)

    try:
        dir = os.path.dirname(path)
        sandbox.filesystem.make_dir(dir)
        sandbox.filesystem.write(path, content)
        # Read back the content to ensure the file was updated
        updated_content = sandbox.filesystem.read(path)
        return updated_content
    except Exception as e:
        return f"Error: {e}"
