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
@patch("helper.get_trunk_branch_name", return_value="current branch")
def test_git_create_branch_happy_case(mock_curr_branch, mock_var, mock_args):
    """
    Function to test gits_create_branch, success case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = create_branch(mock_args)
    assert test_result == True


@patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace(b=None))
@patch("subprocess.Popen")
@patch("helper.get_trunk_branch_name", return_value="current branch")
def test_git_create_branch_sad_case_with_no_branch(mock_curr_branch, mock_var, mock_args):
    """
    Function to test gits_create_branch, failure case with no branch name provided
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = create_branch(mock_args)
    assert test_result == False


@patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace())
@patch("subprocess.Popen")
@patch("helper.get_trunk_branch_name", return_value="current branch")
def test_git_create_branch_sad_case_with_no_arguments(mock_curr_branch, mock_var, mock_args):
    """
    Function to test gits_create_branch, failure case with no arguments passed
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = create_branch(mock_args)
    assert test_result == False
