import os
from dotenv import load_dotenv
from e2b import Sandbox
import openai
import time
from actions import (
    create_directory,
    read_file,
    save_content_to_file,
    list_files,
    commit,
    make_pull_request,
    REPO_DIRECTORY,
)

from rich import print
from rich.console import Console
from rich.theme import Theme
from rich.prompt import Prompt

class MyPrompt(Prompt):
    prompt_suffix = ""


custom_theme = Theme(
    {
        "theme": "bold #666666",
    }
)
console = Console(theme=custom_theme)


load_dotenv()
client = openai.Client()

AI_ASSISTANT_ID = os.getenv("AI_ASSISTANT_ID")
USER_GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

assistant = client.beta.assistants.retrieve(AI_ASSISTANT_ID)

def main():
    # Initial processing for the main function
    work_option = console.input(
        "Select an option to work with [repository/ftp/local]: "
    ).strip().lower()

    if work_option == 'repository':
        # Placeholder for existing repository functionality
        pass
    elif work_option == 'ftp':
        print("FTP option is not currently implemented.")
    elif work_option == 'local':
        print("Local folder option selected.")
    else:
        print("Invalid option selected.")

def prompt_user_for_github_repo():
    # Ask the user for their GitHub repository details
    user_repo = MyPrompt.ask(
        "\nWhat GitHub repo do you want to work in? Specify it like this:\n> your_username/your_repo_name "
    )
    # Removal of stylistic elements for simplicity
    print("\n");
    print("Cloning the repo...")
    print("", end="\n")

    repo_url = f"https://github.com/{user_repo.strip()}.git"

    return repo_url

def prompt_user_for_task(repo_url):
    user_task_specification = MyPrompt.ask(
        "\nWhat do you want to do?\n> "
    )
    # Refactoring the function to retain the essential details and reduce complexity
    user_task = (
        f"Please work with the codebase repo called {repo_url} "
        f"that is cloned in the /home/user/repo directory. React on the following user's comment: {user_task_specification}"
    )
    print("", end="\n")

    return user_task

def prompt_user_for_auth():
    # Retrieving and checking the user's GitHub authentication token
    user_auth = MyPrompt.ask(
        "\nProvide your GitHub token here:\nToken:",
        password=True,
    )
    # Simplified messages to directly communicate requirements
    print("", end="\n")
    return user_auth

def setup_git(sandbox):
    # Configuring user authenticity in git and GitHub
    setup_git_commands = [
        "git config --global user.email 'ai-developer@email.com'",
        "git config --global user.name 'AI Developer'",
        f"echo {USER_GITHUB_TOKEN} | gh auth login --with-token",
        "gh auth setup-git"
    ]
    for cmd in setup_git_commands:
        proc = sandbox.process.start_and_wait(cmd)
        if proc.exit_code != 0:
            print(f"Error during '{cmd}': {proc.stderr}")
            return False
    print("GitHub authentication setup complete.")
    return True

def clone_repo_in_sandbox(sandbox, repo_url):
    # Clone the specified GitHub repository into the sandbox environment
    git_clone_cmd = f"git clone {repo_url} {REPO_DIRECTORY}"
    git_clone_proc = sandbox.process.start_and_wait(git_clone_cmd)
    if git_clone_proc.exit_code != 0:
        print("Error cloning the repo: {git_clone_proc.stderr}")
        return False
    print("Repository cloned successfully.")
    return True

def handle_sandbox_stdout(message):
    # Streamlining message handling for the standard output
    console.print(message.line)

def handle_sandbox_stderr(message):
    # Streamlining message handling for the standard error output
    console.print(message.line)

def main():
    # Incorporate the setup process into the main execution flow for clarity
    if USER_GITHUB_TOKEN is None:
        USER_GITHUB_TOKEN = prompt_user_for_auth()
    if not setup_git(sandbox):
        return
    
    repo_url = prompt_user_for_github_repo()
    if not clone_repo_in_sandbox(sandbox, repo_url):
        return

    # Process user tasks in a loop until completion
    user_task = prompt_user_for_task(repo_url)
    # Adding functionality for handling different user scenarios
    while True:
        # Handling user input and performing actions accordingly
        # Running the AI thread based on user input and managing output
        thread = client.beta.threads.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Carefully plan this task and start working on it: {user_task} in the {repo_url} repo",
                },
            ],
        )
        run = client.beta.threads.runs.create(
            thread_id=thread.id, assistant_id=assistant.id
        )

        while run.status not in ["completed", "cancelled", "expired", "failed"]:
            if run.status == "requires_action":
                outputs = sandbox.openai.actions.run(run)
                client.beta.threads.runs.submit_tool_outputs(
                    thread_id=thread.id, run_id=run.id, tool_outputs=outputs
                )
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id, run_id=run.id
            )
            time.sleep(0.5)

        if run.status == "completed":
            messages = client.beta.threads.messages.list(thread_id=thread.id).data[0].content
            text_messages = [message for message in(messages if message.role == "system")]
            console.print("Task completed:", text_messages[0].text.value)


if __name__ == "__main__":
    main()
