import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_create_branch import create_branch
from mock import patch, Mock


def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)


@patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace(b="branch name"))
@patch("subprocess.Popen")
def test_git_create_branch_happy_path(mock_popen, mock_args):
    """
    Function to test gits_create_branch, success case
    """
    mock_args = parse_args(mock_args)
    test_result = create_branch(mock_args)
    assert test_result == True
