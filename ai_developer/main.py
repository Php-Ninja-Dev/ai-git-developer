"""
AI DEVELOPER
main.py
github.com/natzar/ai-developer

"""
import os
from dotenv import load_dotenv
from e2b import Sandbox
from rich import print
from rich.console import Console
from rich.theme import Theme
from rich.prompt import Prompt
import openai
from ai_developer.task_handler import TaskHandler
from ai_developer.actions import (
    create_directory,
    read_file,
    save_content_to_file,
    list_files,
    commit,
    make_pull_request,
    REPO_DIRECTORY,
    git_pull,
)

# Defaults

user_repo = None

class MyPrompt(Prompt):
    prompt_suffix = ""

custom_theme = Theme(
    {
        "theme": "bold #666666",
    }
)
console = Console(theme=custom_theme)

# Load .env data
load_dotenv()

# Open AI
client = openai.Client()

# Open AI assistant
assistant = client.beta.assistants.retrieve(os.getenv("AI_ASSISTANT_ID"))


def prompt_user_for_github_repo():
    global user_repo
    user_repo = MyPrompt.ask(
        "\nWhat GitHub repo do you want to work in? Specify it like this: [bold #E0E0E0]your_username/your_repo_name[/bold #E0E0E0].\n> "
    )
    print("\n🔄[#666666] Cloning the repo...[/#666666]", end="\n")
    print("", end="\n")

    repo_url = f"https://github.com/{user_repo.strip()}.git"

    return repo_url


def prompt_user_for_task(repo_url):
    user_task_specification = MyPrompt.ask(
        "\n\n🤖[#E57B00][bold] The AI developer is working in the cloned repo[/bold][/#E57B00]\n\nWhat do you want to do?\n> "
    )
    user_task = (
        f"Please work with the codebase repo called {repo_url} "
        f"that is cloned in the /home/user/repo directory. React on the following user's comment: {user_task_specification}"
    )
    print("", end="\n")
    return user_task


def prompt_user_for_auth():
    user_auth = MyPrompt.ask(
        "\nProvide [bold]GitHub token[/bold] with following permissions:\n\n\u2022 read:org\n\u2022 read:project\n\u2022 repo\n\nFind or create your token at [bold #0096FF]https://github.com/settings/tokens[/bold #0096FF]\n\nToken:",
        password=True,
    )
    print("", end="\n")
    return user_auth


def setup_git(sandbox, USER_GITHUB_TOKEN):
    print("Logging into GitHub...")
    # Identify AI developer in git
    sandbox.process.start_and_wait(
        "git config --global user.email 'ai-developer@email.com'"
    )
    sandbox.process.start_and_wait("git config --global user.name 'AI Developer'")

    # Login user to GitHub
    proc = sandbox.process.start_and_wait(
        f"echo {USER_GITHUB_TOKEN} | gh auth login --with-token"
    )
    if proc.exit_code != 0:
        print(
            "[bold #FF0000][Sandbox] [/bold #FF0000]Error: Unable to log into GitHub",
            end="\n",
        )
        print(proc.stderr)
        print(proc.stdout)
        exit(1)

    # Setup user's Git credentials
    proc = sandbox.process.start_and_wait("gh auth setup-git")
    if proc.exit_code != 0:
        print(
            "[bold #FF0000][Sandbox] [/bold #FF0000]Error: Unable to set up Git auth with GitHub"
        )
        print(proc.stderr)
        print(proc.stdout)
        exit(1)
    else:
        print("\n✅ [#666666]Logged in[/#666666]")


def clone_repo_in_sandbox(sandbox, repo_url):
    # Clone the repo
    git_clone_proc = sandbox.process.start_and_wait(
        f"git clone {repo_url} {REPO_DIRECTORY}"
    )
    if git_clone_proc.exit_code != 0:
        print("[bold #FF0000][Sandbox] [/bold #FF0000]Error: Unable to clone the repo")
        exit(1)


def handle_sandbox_stdout(message):
    console.print(f"[theme][Sandbox][/theme] {message.line}")


def handle_sandbox_stderr(message):
    console.print(f"[theme][Sandbox][/theme] {message.line}")


def display_help_menu():
    console.print("Help Menu:")
    console.print("- quit: Exit the program")
    console.print("- restart: Restart the program from the beginning")
    console.print("- <task description>: Describe a new task for the AI developer")


def main():
    """Perform setup and main loop."""

    print("\n🤖[#E57B00][bold] AI developer[/#E57B00][/bold]")

    if os.getenv("E2B_API_KEY") is None:
        print("\n👎[#666666]E2B API key not loaded[/#666666]\n")

    if os.getenv("OPENAI_API_KEY") is None:
        print("\n👎 [#666666]OpenAI key not loaded[/#666666]\n")

    if os.getenv("AI_ASSISTANT_ID") is None:
        print("\n👎 [#666666]OpenAI Assistant ID not loaded[/#666666]\n")

    if os.getenv("GITHUB_TOKEN") is None:
        print("\n✅ [#666666]GitHub token loaded[/#666666]\n")

    # Create the E2B sandbox
    sandbox = Sandbox(
        on_stderr=handle_sandbox_stderr,
        on_stdout=handle_sandbox_stdout,
    )

    # Link actions.py methods to sandbox
    sandbox.add_action(create_directory).add_action(read_file).add_action(
        save_content_to_file
    ).add_action(list_files).add_action(commit).add_action(
        make_pull_request
    ).add_action(
        git_pull
    )

    # Setup git right away so user knows immediatelly if they passed wrong
    # token
    setup_git(sandbox, os.getenv("GITHUB_TOKEN"))

    # Clone repo
    repo_url = prompt_user_for_github_repo()
    clone_repo_in_sandbox(sandbox, repo_url)

    # New Task Handler
    task_handler = TaskHandler(client, sandbox, assistant, console)

    # main loop
    while True:
        # Ready for new task
        user_task = prompt_user_for_task(repo_url)
        task_handler.handle_new_task(user_task, repo_url)


if __name__ == "__main__":
    main()
