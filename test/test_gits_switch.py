import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_switch import switch_branch
from mock import patch, Mock


def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(branch_name="branch name"))
@patch("subprocess.Popen")
def test_gits_switch_happy_case(mock_var, mock_args):
    """
    Function to test gits switch, success case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = switch_branch(mock_args)
    assert True == test_result, "Normal case"


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace())
@patch("subprocess.Popen")
def test_gits_switch_sad_case(mock_var, mock_args):
    """
    Function to test gits switch, failure case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = switch_branch(mock_args)
    assert False == test_result, "Normal case"
