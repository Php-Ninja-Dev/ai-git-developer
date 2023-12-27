def login_wordpress_admin(sandbox: Sandbox, args: Dict[str, Any]) -> str:
def save_content_to_file(path: str, content: str, mode: str = 'overwrite', line_number: int = None) -> None:
    """Save content to a file, with the option to append, insert, or overwrite.

    Args:
        path (str): The path to the file, including extension.
        content (str): The content to save.
        mode (str): The mode of saving the file. Options: 'append', 'insert', 'overwrite'. Default is 'overwrite'.
        line_number (int, optional): The line number where to insert the content if mode is 'insert'.
    """
    try:
        if mode == 'insert' and line_number is not None:
            with open(path, 'r') as file:
                lines = file.readlines()
            with open(path, 'w') as file:
                lines.insert(line_number - 1, content)
                file.writelines(lines)
        else:
            with open(path, mode='a' if mode == 'append' else 'w') as file:
                file.write(content)
        print(f'Content saved in {{mode}} mode to {path}')
    except Exception as e:
        print(f'Error saving content to {path}: {e}')

    """Save content to a file, with the option to append, insert, or overwrite.

    Args:
        path (str): The path to the file, including extension.
        content (str): The content to save.
        mode (str): The mode of saving the file. Options: 'append', 'insert', 'overwrite'. Default is 'overwrite'.
    """
    try:
        with open(path, mode='a' if mode == 'append' else 'w') as file:
            file.write(content)
        print(f'Content saved in {{mode}} mode to {path}')
    except Exception as e:
        print(f'Error saving content to {path}: {e}')

    # Args:
    #     sandbox: The sandbox instance
    #     args: A dictionary containing:
    #           'admin_url': The URL of the admin panel
    #           'username': The admin username
    #           'password': The admin password
    url = args['admin_url']
    username = args['username']
    password = args['password']
    print_sandbox_action('Attempting to login to WordPress Admin at', url)

    try:
        browser = sandbox.webdriver.start()
        browser.get(url)
        browser.find_element_by_id('user_login').send_keys(username)
        browser.find_element_by_id('user_pass').send_keys(password)
        browser.find_element_by_id('wp-submit').click()

        # Check if login was successful by looking for the dashboard identifier
        if "dashboard" in browser.page_source.lower():
            return 'Login successful'
        else:
            return 'Login failed'

        browser.quit()
    except Exception as e:
        browser.quit()
        return f"Error: {e}"

