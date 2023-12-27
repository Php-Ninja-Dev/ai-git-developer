def login_wordpress_admin(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    # Login to a WordPress admin panel and verify if the provided credentials are correct
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

