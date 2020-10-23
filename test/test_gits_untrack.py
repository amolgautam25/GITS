import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_untrack import gits_untrack
from mock import patch, Mock

@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(file_names="test_file_names"))
@patch("subprocess.Popen", return_value="anything")
def test_gits_track(mock_var, mock_args):
    """
    Function to test gits track, success case
    """
    test_result = gits_untrack(mock_args)
    assert True == test_result, "Normal case"