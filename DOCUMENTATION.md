## Documention

This document outlines the necessary steps and provides guidance for setting up and using the AI Developer assistant.

The AI Developer is essentially a sophisticated framework that leverages the capabilities of GPT-4-Turbo to assist developers in working with their codebases in the cloud. Originating from an example by E2B-dev, it has been transformed into a much more versatile and powerful tool.

### Initial Steps
1. First, make sure you have the Git Command Line Interface (gh) installed as it is required to operate the AI Developer. You can install it by following these commands:
```sh
sudo apt update
sudo apt install gh
```
2. Clone the repository where AI Developer is hosted.
3. Navigate to the directory where you cloned the repo, and specifically to the ai-github-developer directory.
4. Follow the instructions in the README for setting up the environment and dependencies.

### Setup

After you have the code and the necessary tools, you'll need to

1. Ensure your `.env` is properly configured with the necessary API keys.
2. Create an AI assistant by executing `poetry run create-ai-assistant`. This is a mandatory step as you will need the assistant ID for proper configuration.
3. Set the assistant ID in your `.env` file and make sure it is correctly referenced by the application.

After completing these steps, you will have set up the AI Developer successfully.

### Usage

Refer to the README.md for instructions on how to start and use your new AI developer assistant to manage your codebase tasks efficiently and effectively.
