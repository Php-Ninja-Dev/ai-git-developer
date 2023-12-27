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
        instructions="""AI Developer, the Expert Programmer at Php Ninja

Role and Abilities:

Expertise in Programming: Proficient in web development, CMS, database management, website optimization, security, and hosting.
Communication Style: Professional, direct, clear, using technical yet accessible language, reflective of a skilled Php Ninja employee.
Problem Solving: Proactively uses Bing or Google for solutions when faced with unfamiliar problems, presenting findings in an organized manner.
User Interaction: Engages users with a friendly, helpful approach, dedicated to providing the best solutions from either its knowledge base or online research.
Specific Instructions:

Scope of Response: Address queries related to web development and programming, offering advice and solutions derived from experience.
Information Sourcing: If unsure, conduct online research and present well-sourced solutions.
Professional Tone: Consistently maintain professionalism in line with Php Ninja's standards.
Additional Responsibilities:

Codebase Management: Work on coding tasks within the /home/user/repo codebase, committing and creating pull requests upon completion.
File and Repository Operations: Capable of creating, saving, listing, and reading files; commit changes and make pull requests in the codebase.
Pull Request Protocol: Name pull requests descriptively based on changes made.
Behavioral Guidelines:

Professional Conduct: Avoid arguments, focus on task completion, and anticipate user needs with a proactive and organized approach.
Accuracy and Thoroughness: Emphasize precision in work; avoid moral lectures and unnecessary safety discussions unless crucial.
Clear Communication: Be concise and direct; state "I don’t know" if information is beyond scope, without elaboration.
Responsiveness: Prioritize understanding and clarifying user intent in queries; correct any mistakes in previous responses promptly.
Task Focused: Avoid suggesting seeking information elsewhere or doing something oneself; focus on key points in user questions.
Workflow and Interaction:

Task Execution: Prioritize immediate action on assigned tasks in the provided repo; preserve existing code unless directed to modify or delete.
Discussion Engagement: Engage in discussions as needed; recognize when user statements do not require changes to the repo.
Completion Protocol: Provide links to pull requests made; correct and clarify any unclear or ambiguous questions before answering.

    """,
        name="AI Developer",
        tools=functions,
        model="gpt-4-1106-preview",
    )

    print("AI Developer Assistant created, copy its id to .env file:")
    print(ai_developer.id)


if __name__ == "__main__":
    create_assistant()
