import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_status import gits_status
from mock import patch, Mock


def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace())
@patch("subprocess.Popen")
def test_gits_track_happy_case(mock_var, mock_args):
    """
    Function to test gits status, success case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output'.encode('UTF-8'), 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_status(mock_args)
    assert True == test_result, "Normal case"


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace())
@patch("subprocess.Popen")
def test_gits_track_sad_case(mock_var, mock_args):
    """
    Function to test gits status, failure case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_status(mock_args)
    assert False == test_result