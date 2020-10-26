import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_commit import gits_commit_func
from mock import patch, Mock


def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(m="test_commit", amend=True))
@patch("subprocess.Popen")
def test_gits_commit_happy_case_with_amend(mock_var, mock_args):
    """
    Function to test gits_commit, success case with amend message
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_commit_func(mock_args)
    assert True == test_result, "Normal case"


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(m="test_commit", amend=False))
@patch("subprocess.Popen")
def test_gits_commit_happy_case_without_amend(mock_var, mock_args):
    """
    Function to test gits_commit, success case with no amend message
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_commit_func(mock_args)
    assert True == test_result, "Normal case"


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(m=None, amend=False))
@patch("subprocess.Popen")
def test_gits_commit_sad_case_with_no_message(mock_var, mock_args):
    """
    Function to test gits_commit, failure case with no commit message
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_commit_func(mock_args)
    assert False == test_result


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace())
@patch("gits_logging.gits_logger")
def test_gits_commit_sad_case_with_no_arguments(mock_err, mock_args):
    """
    Function to test gits_commit, failure case with no arguments passed
    """
    mock_args = parse_args(mock_args)
    test_result = gits_commit_func(mock_args)
    assert False == test_result
