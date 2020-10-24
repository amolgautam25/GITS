import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_track import gits_track
from mock import patch, Mock


def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(file_names=["test1", "test2"]))
@patch("subprocess.Popen", return_value="anything")
def test_gits_track(mock_var, mock_args):
    """
    Function to test gits track, success case
    """
    mock_args = parse_args(mock_args)
    test_result = gits_track(mock_args)
    assert True == test_result, "Normal case"