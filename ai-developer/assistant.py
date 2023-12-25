from typing import List

from dotenv import load_dotenv
import openai
from openai.types.beta.assistant_create_params import Tool

load_dotenv()


def create_assistant():
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
                        },
                    },
                    "required": ["content", "path"],
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
        instructions="""You are an AI developer. You help user work on their tasks related to coding in their codebase. The provided codebase is in the /home/user/repo.
    When given a coding task, work on it until completion, commit it, and make pull request.

    If you encounter a problem, communicate it promptly, please.

    You can create and save content (text or code) to a specified file (or create a new file), list files in a given directory, read files, commit changes, and make pull requests. Always make sure to write the content in the codebase.

    By default, always either commit your changes or make a pull request after performing any action on the repo. This helps in reviewing and merging your changes.
    Name the PR based on the changes you made.

    Be professional, avoid arguments, and focus on completing the task.

    When you finish the task, always provide the link to the pull request you made (if you made one.)
    Additionally, be prepared for discussions; not everything user writes implies changes to the repo. For example, if the user writes "thank you", you can simply answer "you are welcome".
    But by default, if you are assigned a task, you should immediately do it in the provided repo, and not talk only talk about your plan.
    """,
        name="AI Developer",
        tools=functions,
        model="gpt-4-1106-preview",
    )

    print("AI Developer Assistant created, copy its id to .env file:")
    print(ai_developer.id)


if __name__ == "__main__":
    create_assistant()

                {
                    "type": "function",
                    "function": {
                        "name": "rollback",
                        "description": "Roll back to a specific commit",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "commit_hash": {
                                    "type": "string",
                                    "description": "The hash of the commit to roll back to"
                                }
                            },
                            "required": ["commit_hash"]
                        }
                    }
                },
                {
                    "type": "function",
                    "function": {
                        "name": "reset",
                        "description": "Reset the current HEAD to the specified state",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "mode": {
                                    "type": "string",
                                    "description": "Can be 'soft', 'mixed', or 'hard'"
                                }
                            },
                            "required": ["mode"]
                        }
                    }
                },
                {
                    "type": "function",
                    "function": {
                        "name": "cherrypick",
                        "description": "Apply the changes introduced by some existing commits",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "commit_hash": {
                                    "type": "string",
                                    "description": "The hash of the commit to cherry-pick"
                                }
                            },
                            "required": ["commit_hash"]
                        }
                    }
                }

# Entry for the new send_email functionality in the assistant's workflow
from typing import List

from dotenv import load_dotenv
import openai
from openai.types.beta.assistant_create_params import Tool

load_dotenv()
def create_assistant():
    client = openai.Client()

    functions: List[Tool] = [
        # Existing functions
        # ... (Other existing functions have not been modified and should remain as is)
        {
            "type": "function",
            "function": {
                "name": "send_email",
                "description": "Send an email",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "smtp_server": {
                            "type": "string",
                            "description": "SMTP server address"
                        },
                        "smtp_port": {
                            "type": "integer",
                            "description": "SMTP port number"
                        },
                        "username": {
                            "type": "string",
                            "description": "Username for SMTP authentication"
                        },
                        "password": {
                            "type": "string",
                            "description": "Password for SMTP authentication"
                        },
                        "sender": {
                            "type": "string",
                            "description": "Email address of the sender"
                        },
                        "recipients": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of recipient email addresses"
                        },
                        "subject": {
                            "type": "string",
                            "description": "Subject of the email"
                        },
                        "body": {
                            "type": "string",
                            "description": "Body content of the email"
                        }
                    },
                    "required": ["smtp_server", "smtp_port", "username", "password", "sender", "recipients", "subject", "body"]
                }
            }
        }
    ]

    # ... (Rest of the assistant creation code)

if __name__ == "__main__":
    create_assistant()

def append_content_to_file(*args, **kwargs):
    return actions.append_content_to_file(*args, **kwargs)
from typing import List

from dotenv import load_dotenv
import openai
from openai.types.beta.assistant_create_params import Tool

load_dotenv()


def create_assistant():
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
        # ... (Rest of the existing functions)
        {
            "type": "function",
            "function": {
                "name": "send_email",
                "description": "Send an email",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "smtp_server": {
                            "type": "string",
                            "description": "SMTP server address"
                        },
                        "smtp_port": {
                            "type": "integer",
                            "description": "SMTP port number"
                        },
                        "username": {
                            "type": "string",
                            "description": "Username for SMTP authentication"
                        },
                        "password": {
                            "type": "string",
                            "description": "Password for SMTP authentication"
                        },
                        "sender": {
                            "type": "string",
                            "description": "Email address of the sender"
                        },
                        "recipients": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of recipient email addresses"
                        },
                        "subject": {
                            "type": "string",
                            "description": "Subject of the email"
                        },
                        "body": {
                            "type": "string",
                            "description": "Body content of the email"
                        }
                    },
                    "required": ["smtp_server", "smtp_port", "username", "password", "sender", "recipients", "subject", "body"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "rollback",
                "description": "Roll back to a specific commit",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "commit_hash": {
                            "type": "string",
                            "description": "The hash of the commit to roll back to"
                        }
                    },
                    "required": ["commit_hash"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "reset",
                "description": "Reset the current HEAD to the specified state",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mode": {
                            "type": "string",
                            "description": "Can be 'soft', 'mixed', or 'hard'"
                        }
                    },
                    "required": ["mode"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "cherrypick",
                "description": "Apply the changes introduced by some existing commits",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "commit_hash": {
                            "type": "string",
                            "description": "The hash of the commit to cherry-pick"
                        }
                    },
                    "required": ["commit_hash"]
                }
            }
        }
    ]

    ai_developer = client.beta.assistants.create(
        instructions="""You are an AI developer. You help user work on their tasks related to coding in their codebase. The provided codebase is in the /home/user/repo.
    When given a coding task, work on it until completion, commit it, and make pull request.

    If you encounter a problem, communicate it promptly, please.

    You can create and save content (text or code) to a specified file (or create a new file), list files in a given directory, read files, commit changes, and make pull requests. Always make sure to write the content in the codebase.

    By default, always either commit your changes or make a pull request after performing any action on the repo. This helps in reviewing and merging your changes.
    Name the PR based on the changes you made.

    Be professional, avoid arguments, and focus on completing the task.

    When you finish the task, always provide the link to the pull request you made (if you made one.)
    Additionally, be prepared for discussions; not everything user writes implies changes to the repo. For example, if the user writes "thank you", you can simply answer "you are welcome".
    But by default, if you are assigned a task, you should immediately do it in the provided repo, and not talk only talk about your plan.
    """,
        name="AI Developer",
        tools=functions,
        model="gpt-4-1106-preview",
    )

    print("AI Developer Assistant created, copy its id to .env file:")
    print(ai_developer.id)


if __name__ == "__main__":
    create_assistant()
