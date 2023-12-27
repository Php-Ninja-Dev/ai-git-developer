# Repository Selection

This repository provides an interface for the AI developer to interact with different 
storage options for managing the codebases. Currently, the AI developer can work with
three types of storage:

1. GitHub Repository (Remote)
2. FTP Server (Remote)
3. Local Filesystem (Either remote or local depending on the execution environment)

The user will be prompted to select the type of storage they prefer when initiating 
their tasks. It is crucial to set up the appropriate access tokens and credentials 
for GitHub and FTP to ensure seamless operation.

## Update for Selection Process

We have now updated the selection process to make it more intuitive for the user. 
When prompted, the user will select their desired repository by entering:

- `1` for GitHub Repository
- `2` for FTP Server
- `3` for Local Filesystem

The system will then proceed based on the user's selection and provide prompts for
the necessary information for that specific storage type. This new process aims to
streamline the setup and ensure that the AI developer can access the specified
storage without any issues.

Your system prompt or instructions go here