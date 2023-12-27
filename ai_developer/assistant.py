'''Module for the AI Developer assistant'''

import dotenv
import openai
from openai.types.beta.assistant_create_params import AssistantCreateParams

import openai
from openai.types.beta.assistant_create_params import Tool

"""AI Developer assistant class."""



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
                "name": "modify_file_line",
"""Main module for the AI Developer assistant."""

                "parameters": {
                    "type": "object",
                    "properties": {
                        "new_content": {
                            "type": "string",
                            "description": "New content for defined line",
                        },
                        "line_number": {
                            "type": "integer",
                            "description": "File line number",
                        },
                        "path": {
                            "type": "string",
                            "description": "The path to the file, including extension",
                        },
                    },
                    "required": ["line_number", "new_content","path"],
                },
            },
        },
        {
        "type": "function",
            "function": {
                "name": "send_email",
       			"descruotuin": "Send email to recipients",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipients": {
                            "type": "array",
                            "items": { "type": "string" },
                            "description": "List of email recipients"
                        },
                        "subject": {
                            "type": "string",
                            "description": "The subject line of the email"
                        },
                        "body": {
                            "type": "string",
                            "description": "The body content of the email"
                        }
                    },
                    "required": ["recipients", "subject", "body"],
                }
            }
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
                "name": "git_pull",
                "description": "Pull changes from repo origin",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "branch": {
                            "type": "string",
                            "description": "The branch to pull from, defaulting to main"
                        }
                    },
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "download_ftp_folder",
                "description": "Download a folder via FTP",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message": {
                            "type": "string",
                            "description": "The commit message"
                        }
                    },
                    "required": ["ftp_server","ftp_path","local_path","username","password"]
                }
            }
        },
        {

            "type": "function",
            "function": {
                "name": "check_git_status",
                "description": "Checks the git status of the repo",
                "parameters": {
                    "type": "object",
"""Performs the specified action based on user input."""

                        
                    },
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "find_replace_in_file",
                "description": "Finds and replaces text within a file",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "The path of the file"
                        },
                        "find": {
                            "type": "string",
                            "description": "The text to find"
                        },
                        "replace": {
                            "type": "string",
                            "description": "The text to replace it with"
                        }
                    },
                    "required": ["path", "find", "replace"]
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "rename_file",
                "description": "Renames a specified file within the system",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "old_path": {
                            "type": "string",
                            "description": "The current path of the file"
                        },
                        "new_path": {
                            "type": "string",
                            "description": "The new path (including new file name) of the file"
                        }
                    },
                    "required": ["old_path", "new_path"]
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "copy_file",
                "description": "Copies a file within the system",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "src_path": {
                            "type": "string",
                            "description": "The source path of the file to copy"
                        },
                        "dest_path": {
                            "type": "string",
                            "description": "The destination path of the file"
                        },
                    },
                    "required": ["src_path", "dest_path"]
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "delete_file",
                "description": "Deletes a specified file from the system",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "The path of the file to delete"
                        },
                    },
                    "required": ["path"]
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
"""Handles user input and executes appropriate actions."""

    ai_developer = client.beta.assistants.create(
        instructions="""You are an AI developer. You help the user work on their tasks related to coding in their codebase. The provided codebase is in the /home/user/repo.
    When given a coding task, work on it until completion, commit it, and make a pull request. Treat files very carefully, never remove other lines unless asked for it, think carefully about where your new lines should go relative to other lines in the file, and never overwrite without a reason.

    If you encounter a problem, communicate it promptly, please.

    You can create and save content (text or code) to a specified file (or create a new file), list files in a given directory, read files, commit changes, modify file lines, send emails, and make pull requests. Always make sure to write the content in the codebase.

    By default, always either commit your changes or make a pull request after performing any action on the repo. This helps in reviewing and merging your changes.
    Name the PR based on the changes you made.

    Be professional, avoid arguments, and focus on completing the task.
    When modifying existing code, ensure that your changes maintain the integrity and functionality of the codebase. Provide clear explanations for any modifications or decisions that depart from the original implementation. For new code blocks, evaluate the context and structure of the existing codebase to determine the most appropriate location for additions. 

    Draft commit messages that succinctly and clearly describe the changes made. For tasks with multiple components or that evolve over time, update the status of the task in the commit message, indicating progress, completions, or blockers.

    In cases where a task is ambiguous or has multiple facets, seek to clarify the requirements with the task provider or make incremental progress on aspects that are clear, while communicating the need for further direction on uncertain parts.

    When you finish the task, always provide the link to the pull request you made (if you made one.)
    Additionally, be prepared for discussions; not everything the user writes implies changes to the repo. For example, if the user writes "thank you", you can simply answer "you are welcome".
    But by default, if you are assigned a task, you should immediately do it in the provided repo, execute the plan and don't tell me about it.
    """,
        name="AI Developer",
        tools=functions,
        model="gpt-4-1106-preview",
    )

    print("AI Developer Assistant created, copy its id to .env file:")
    print(ai_developer.id)


if __name__ == "__main__":
    create_assistant()
