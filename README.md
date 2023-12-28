# AI Developer
[![License: GPL3](https://img.shields.io/github/license/natzar/ai-developer)](https://github.com/natzar/ai-developer/blob/main/LICENSE.md)
> 🚧 **Note**: This project is in early development. Use in production environments is not recommended.

DISCLAIMER: Based on [e2b dev cookbook example](https://github.com/e2b-dev/e2b-cookbook/tree/main/guides/ai-github-developer-py), made by [Tereza Tizkova](https://twitter.com/tereza_tizkova), [discovered on twitter](https://twitter.com/tereza_tizkova/status/1737185638141644995) [by @betoayesa](https://twitter.com/betoayesa) who did not wait much on cloning the repo to try to extend it.

![Gif from developer](assets/run_example.gif)

An AI assistant for developers, originally based on a example from  [E2B-dev](https://e2b.dev) 

A custom AI assistant that can clone any GitHub repository to its remote cloud environment, work on the repo there, and then make pull request to GitHub.

The AI developer uses E2B sandboxes for the remote execution of tasks. We acknowledge the initial example provided by E2B-dev, which has been extensively customized and expanded for this project.

### Features
- Works directly any GitHub repository and makes a PR once done
- AI can clone the repo and edit, read, and write files
- Controllable from your terminal
- Powered by GPT-4-Turbo
- Runs in secure cloud [sandbox](https://e2b.dev/docs) by E2B

## Requirements
- Python v3
- Poetry: curl -sSL https://install.python-poetry.org | python3 -
- Github CLI Client: https://github.com/cli/cli#installation 
- OpenAi API key: https://platform.openai.com
- Github Api key: https://github.com/settings/tokens
- OpenAi Assistant Id: Keep reading
- e2b api key: https://e2b.dev/docs/getting-started/api-key

## How to start
1. Clone this repository
2. Install dependencies: Poetry, Git cli,
```sh
poetry install
sudo apt update; sudo apt install gh OR brew install gh OR check [url]

```
3. Rename `.env.example` to `.env` and set up the `OPENAI_API_KEY` key and the `E2B_API_KEY` key. You can get `E2B_API_KEY` at  https://e2b.dev/docs/getting-started/api-key
4. Run `poetry run create-ai-assistant` to create a new AI assistant, which is mandatory for the setup.
5. Get the assistant ID from the console output and set it in the `.env` file as `AI_ASSISTANT_ID`
6. Start the app:
```sh
poetry run start
```
# Authors

- Tereza Tizkova https://twitter.com/tereza_tizkova for e2b.dev
- Beto Ayesa

# Roadmap

- Prepare the bases for openning it to contributions.
- Fixing pylint errors to automatize workflow

- Fix AI Developer file modifications management (Most important first step)

# Contribute

Read contributions guidelines and start creating pull requests.

# Get Help
Please create an issue here in github


# License

GPL-3. Check LICENSE.md

