def save_content_to_file(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    path = args["path"]
    content = args["content"]
    mode = args.get("mode", "overwrite")
    line_number = args.get("line_number")

    print_sandbox_action("Saving content", f"mode={mode}, path={path}")

    try:
        _dir = os.path.dirname(path)
        sandbox.filesystem.make_dir(_dir)

        if mode == "append":
            sandbox.filesystem.append(path, content)
        elif mode == "insert":
            sandbox.filesystem.insert(path, content)
        elif mode == "modify_line":
            if line_number is not None:
                sandbox.filesystem.modify_line(path, line_number, content)
            else:
                return "Error: line_number is required when mode is modify_line"
        else:
            sandbox.filesystem.write(path, content)

        return "success"
    except Exception as e:
        return f"Error: {e}"

