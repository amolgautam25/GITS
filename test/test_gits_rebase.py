import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_rebase import gits_rebase
from mock import patch, Mock


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace())
@patch("subprocess.Popen")
@patch("builtins.input", return_value="yes")
def test_gits_rebase_happy_case_current_branch(mock_input, mock_var, mock_args):
    """
    Function to test gits rebase, success case with rebase on current branch
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output'.encode('UTF-8'), 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    test_result = gits_rebase(mock_args)
    assert True == test_result, "Normal case"


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace())
@patch("subprocess.Popen")
@patch("builtins.input", side_effect=["no", "branch name"])
def test_gits_rebase_happy_case_given_branch(mock_input, mock_var, mock_args):
    """
    Function to test gits rebase, success case with rebase on given branch
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output'.encode('UTF-8'), 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    test_result = gits_rebase(mock_args)
    assert True == test_result, "Normal case"


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace())
@patch("subprocess.Popen")
@patch("builtins.input", side_effect=["no", "branch name"])
def test_gits_rebase_sad_case(mock_input, mock_var, mock_args):
    """
    Function to test gits rebase, failure case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    test_result = gits_rebase(mock_args)
    assert False == test_result, "Normal case"
