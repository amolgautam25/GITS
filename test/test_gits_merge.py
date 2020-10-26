import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_merge import merge_branch
from mock import patch, Mock


def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)


@patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace(branch_name="branch name"))
@patch("subprocess.Popen")
def test_git_create_branch_happy_case(mock_var, mock_args):
    """
    Function to test gits_merge_branch, success case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = merge_branch(mock_args)
    assert test_result == True


@patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace())
def test_git_create_branch_sad_case(mock_args):
    """
    Function to test gits_merge_branch, failure case when no arguments
    """
    mock_args = parse_args(mock_args)
    test_result = merge_branch(mock_args)
    assert test_result == False