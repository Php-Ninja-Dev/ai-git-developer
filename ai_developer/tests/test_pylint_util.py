import unittest
from ai_developer.utils.pylint_util import run_pylint

class TestPylint(unittest.TestCase):
    """ Unit tests for Pylint utility. """

    def test_pylint_runs(self):
        """ Test that Pylint runs without errors on given files. """
        files_to_test = [
            'assistant.py',
            'main.py',
        ]

        # Call the Pylint runner utility function
        run_pylint(files_to_test)

if __name__ == '__main__':
    unittest.main()
