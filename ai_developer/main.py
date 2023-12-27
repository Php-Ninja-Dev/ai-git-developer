import os
from dotenv import load_dotenv
from e2b import Sandbox
import openai
import html
import time
from ai_developer.actions import (
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
    should_restart = True
    while should_restart:
        should_restart = run_cli()

        if should_restart:
            # Clear environment
            for key in list(os.environ):
                if key.startswith('SANDBOX_ACTION_'):
                    del os.environ[key]

            console.log("Resetting the program...")

def run_cli():
    global USER_GITHUB_TOKEN

    WORK_OPTIONS = ['repository', 'ftp', 'local', 'reset']
    # ... the rest of the existing code remains unchanged up to the end of the file ...
