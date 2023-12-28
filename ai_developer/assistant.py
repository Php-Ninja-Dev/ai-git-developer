from typing import List
from dotenv import load_dotenv
import openai
from openai.types.beta.assistant_create_params import Tool

load_dotenv()


def create_assistant():
    """Perform [brief description of the function's action].

    Args:
        param1 (type): Description of param1.
        param2 (type): Description of param2.

    Returns:
        type: Description of return value.

    Raises:
        ErrorType: Description of error.
    """

    client = openai.Client()

    functions: List[Tool] = [
        {
            "type": "function",
            "function": {
                "name": "create_directory",
                "description": "Create a directory",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "The path to the directory to be created",
                        },
                    },
                    "required": ["path"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "save_content_to_file",
                "description": "Save content (code or text) to file",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "content": {
                            "type": "string",
                            "description": "The content to save",
                        },
                        "path": {
                            "type": "string",
                            "description": "The path to the file, including extension",

        {
            "type": "function",
            "function": {
                "name": "git_pull",
                "description": "Executes a git pull command in the specified directory",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "working_directory": {
                            "type": "string",
                            "description": "The working directory where the git pull command should be executed, defaults to REPO_DIRECTORY"
                        }
                    },
                    "required": []
                }
            }
        },
                        },
                        "mode": {
                            "type": "string",
                            "enum": ["insert", "append", "overwrite", "modify_line"],
                            "description": "The mode of file operation (default is overwrite)",
                        },
                        "line_number": {
                            "type": "integer",
                            "description": "The line number to modify, required if mode is modify_line",
                        },
                    },
                    "required": ["mode", "content", "path"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "list_files",
                "description": "List files in a directory",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "The path to the directory",
                        },
                    },
                    "required": ["path"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "read_file",
                "description": "Read a file",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "The path to the file",
                        },
                    },
                    "required": ["path"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "commit",
                "description": "Commit changes to the repo",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message": {
                            "type": "string",
                            "description": "The commit message",
                        },
                    },
                    "required": ["message"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "make_pull_request",
                "description": "Creates a new branch and makes a pull request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description": "The title of the pull request",
                        }
                    },
                    "required": ["title"],
                },
            },
        },
    ]

    ai_developer = client.beta.assistants.create(
        instructions="""You are an AI developer responsible for working on coding tasks in the provided codebase located at /home/user/repo. Here are your core directives:

Task Execution and Committing Changes:

Work on coding tasks until completion, carefully committing changes and making pull requests. Always consider the best position for new or modified code in terms of readability and maintainability.
By default, either commit changes or make a pull request after any action on the repo. Name the pull request based on the changes made.
Code Review and Modification:

Thoroughly review the entire file or relevant code sections before making changes to understand context, dependencies, and potential impact.
Avoid unnecessary code deletion unless justified. Document the reasons for any code removal in commit messages or comments.
Documentation and Testing:

Clearly document any changes made. Write meaningful commit messages and use inline comments to explain complex logic or important decisions.
Test all changes thoroughly to ensure they work as intended without introducing new bugs. This includes unit, integration, and manual testing.
Adherence to Standards and Collaboration:

Follow established coding standards and best practices for the language and framework, adhering to principles like DRY and KISS.
Collaborate effectively with team members, communicate clearly, and be open to feedback. Make frequent, small, and understandable commits.
Security, Privacy, and Continuous Learning:

Consider security and privacy implications in your code, following best practices for data handling and security.
Stay updated with the latest technological developments and be open to learning new methods and tools.
Problem-Solving and Communication:

If you encounter a problem, communicate it promptly.
Be prepared for discussions; not everything the user writes implies changes to the repo. Respond appropriately to non-task-related interactions.
Clarification and Adaptation:

Seek clarification on ambiguous tasks before proceeding. Be adaptable and ready to update your approach based on team needs and feedback.
Remember, your role is to enhance the codebase with precision and care. Be professional, avoid arguments, and focus on completing the task efficiently
    """,
        name="AI Developer",
        tools=functions,
        model="gpt-4-1106-preview",
    )

    print("AI Developer Assistant created, copy its id to .env file:")
    print(ai_developer.id)


if __name__ == "__main__":
    create_assistant()
