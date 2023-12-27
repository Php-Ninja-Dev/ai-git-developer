
# Instructions for user interaction with the AI
# Define AI's capabilities and how the user can utilize them
from rich import print
from rich.console import Console
from rich.theme import Theme
from rich.prompt import Prompt
from dotenv import load_dotenv


# Define a custom theme for console outputs
custom_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "error": "bold red",
    "key": "bold cyan",
    "value": "green",
    "title": "bold underline magenta"
})
console = Console(theme=custom_theme)

# Load environment variables from .env file
load_dotenv()

# Helper function to print error messages
def print_error(error):
    console.print(f"[error]Error: {error}[/error]")

# Create an instance of the console with the custom theme
console = Console(theme=custom_theme)
def run_analysis(repo_path):
    """Run static code analysis on the repo.
    :param repo_path: Path to the repository
    :return: None
    """
    console.print("[title]Running Pylint analysis...[/title]", style="bold")

    pylint_output = os.popen(f'pylint {repo_path}').read()
    console.print(pylint_output, style="key")

# Execute the analysis on the repository
run_analysis('/home/user/repo/ai_developer')