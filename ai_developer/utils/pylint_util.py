""" Utility module for Pylint integration """

import subprocess


def run_pylint(files):
    """ Runs Pylint on a list of files."""
    for file in files:
        # Execute Pylint on each file
        result = subprocess.run(['pylint', file], capture_output=True, text=True)

        # Print the result of Pylint
        print(f"Pylint output for {file}:")
        print(result.stdout)
        print("---\n")
