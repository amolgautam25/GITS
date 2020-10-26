import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_push import gits_push
from mock import patch, Mock


def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(rebase="branch name"))
@patch("subprocess.Popen")
@patch("helper.get_current_branch", return_value="current branch")
def test_gits_push_happy_case_with_rebase(mock_current_branch, mock_var, mock_args):
    """
    Function to test gits push, success case with rebase
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': (b'', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_push(mock_args)
    assert True == test_result, "Normal case"


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(rebase="branch name"))
@patch("subprocess.Popen")
def test_gits_push_sad_case_with_uncommitted_changes(mock_var, mock_args):
    """
    Function to test gits push, failure case with uncommitted changes
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': (b'anything', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_push(mock_args)
    assert False == test_result, "Normal case"


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace())
@patch("subprocess.Popen")
@patch("helper.get_current_branch", return_value="current branch")
def test_gits_push_sad_case_with_no_arguments(mock_current_branch, mock_var, mock_args):
    """
    Function to test gits push, failure case with no arguments
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': (b'', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_push(mock_args)
    assert False == test_result, "Normal case"