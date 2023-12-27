
    {
        "type": "function",
        "function": {
            "name": "cherrypick",
            "description": "Cherry-pick a commit into the current branch",
            "parameters": {
                "type": "object",
                "properties": {
                    "commit_hash": {
                        "type": "string",
                        "description": "The commit hash to cherry-pick"
                    }
                },
                "required": ["commit_hash"]
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
                        "description": "The commit hash to roll back to"
                    }
                },
                "required": ["commit_hash"]
            }
        }
    }
]

ai_developer = client.beta.assistants.create(
    instructions="You are an AI developer. You help user work on their tasks related to coding in their codebase. The provided codebase is in the /home/user/repo
When given a coding task, work on it until completion, commit it, and make pull request.

If you encounter a problem, communicate it promptly, please.

You can create and save content (text or code) to a specified file (or create a new file), list files in a given directory, read files, commit changes, and make pull requests. Always make sure to write the content in the codebase.

By default, always either commit your changes or make a pull request after performing any action on the repo. This helps in reviewing and merging your changes.
Name the PR based on the changes you made.

Be professional, avoid arguments, and focus on completing the task.

When you finish the task, always provide the link to the pull request you made (if you made one.)
Additionally, be prepared for discussions; not everything user writes implies changes to the repo. For example, if the user writes "thank you", you can simply answer "you are welcome".
But by default, if you are assigned a task, you should immediately do it in the provided repo, and not talk only talk about your plan.
",
    name="AI Developer",
    tools=functions,
    model="gpt-4-1106-preview",
)

print("AI Developer Assistant created, copy its id to .env file:")
print(ai_developer.id)