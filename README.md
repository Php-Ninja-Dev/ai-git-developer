# AI Developer

![Gif from developer](assets/run_example.gif)

An AI assistant for developers, originally based on a single example from E2B-dev.

A custom AI assistant that can clone any GitHub repository to its remote cloud environment, work on the repo there, and then make pull request to GitHub.

**Notice: The action `save_content_to_file` overwrites the existing file, hence always ensure to provide the complete updated file content when using this function.**

The AI developer uses E2B sandboxes for the remote execution of tasks. We acknowledge the initial example provided by E2B-dev, which has been extensively customized and expanded for this project.

### Features
- Works directly any GitHub repository and makes a PR once done
- AI can clone the repo and edit, read, and write files
- Controllable from your terminal
- Powered by GPT-4-Turbo
- Runs in secure cloud [sandbox](https://e2b.dev/docs) by E2B


## How to start
1. Clone this repository
2. Open the [e2b-cookbook/guides/ai-github-developer-py](./) directory
3. Install dependencies:
```sh
poetry install
```
4. Install Git Command Line Interface (gh):
```sh
sudo apt update
sudo apt install gh
```
5. Rename `.env.example` to `.env` and set up the `OPENAI_API_KEY` key and the `E2B_API_KEY` key. You can get `E2B_API_KEY` at  https://e2b.dev/docs/getting-started/api-key
6. Run `poetry run create-ai-assistant` to create a new AI assistant, which is mandatory for the setup.
7. Get the assistant ID from the console output and set it in the `.env` file as `AI_ASSISTANT_ID`
8. Start the app:
```sh
poetry run start
```
