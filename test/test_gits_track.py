import argparse
import os
import sys

sys.path.insert(1, os.getcwd())
print(sys.path)

from gits_track import gits_track
from mock import patch, Mock

@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(file_names="test_file_names"))
@patch("subprocess.Popen", return_value="anything")
def test_gits_track(mock_args):
    """
    Function to test gits track, success case
    """
    test_result = gits_track(mock_args)
    assert True == test_result, "Normal case"