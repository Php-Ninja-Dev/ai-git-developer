import pytest
from ai_developer.actions import create_directory


def test_create_directory(self):
    # Test case to create a directory
    response = create_directory("/home/user/repo/tests/test_directory")
    assert response == "success"
