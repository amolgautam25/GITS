import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_pull import gits_pull
from mock import patch, Mock


def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(nocommit=True, rebase=False, branch="branch name"))
@patch("subprocess.Popen")
@patch("helper.get_current_branch", return_value="current branch")
def test_gits_pull_happy_case_with_no_commit_and_given_branch(mock_current_branch, mock_var, mock_args):
    """
    Function to test gits pull, success case with no commits, no rebase and given branch
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': (b'', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_pull(mock_args)
    assert True == test_result, "Normal case"


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(nocommit=True, rebase=False, branch=False))
@patch("subprocess.Popen")
@patch("helper.get_current_branch", return_value="current branch")
def test_gits_pull_happy_case_with_no_commit_and_current_branch(mock_current_branch, mock_var, mock_args):
    """
    Function to test gits pull, success case with no commits, no rebase and given branch
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': (b'', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_pull(mock_args)
    assert True == test_result, "Normal case"


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(nocommit=False, rebase=True, branch="branch name"))
@patch("subprocess.Popen")
@patch("helper.get_current_branch", return_value="current branch")
def test_gits_pull_happy_case_with_commit_and_given_branch(mock_current_branch, mock_var, mock_args):
    """
    Function to test gits pull, success case with commits, rebase and given branch
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': (b'', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_pull(mock_args)
    assert True == test_result, "Normal case"


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(nocommit=True, rebase=True, branch="branch name"))
@patch("subprocess.Popen")
@patch("helper.get_current_branch", return_value="current branch")
def test_gits_pull_sad_case_with_no_commit_and_rebase(mock_current_branch, mock_var, mock_args):
    """
    Function to test gits pull, failure case with no commits, but rebase
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': (b'', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_pull(mock_args)
    assert False == test_result


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(nocommit=True, rebase=True, branch="branch name"))
@patch("subprocess.Popen")
def test_gits_pull_sad_case_with_uncomitted_changes(mock_var, mock_args):
    """
    Function to test gits pull, failure case with uncommited changes
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': (b'anything', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_pull(mock_args)
    assert False == test_result


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace())
@patch("subprocess.Popen")
@patch("helper.get_current_branch", return_value="current branch")
def test_gits_pull_sad_case_with_no_arguments(mock_current_branch, mock_var, mock_args):
    """
    Function to test gits pull, failure case with no arguments passed
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': (b'', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_pull(mock_args)
    assert False == test_result