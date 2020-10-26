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
@patch("subprocess.Popen")
def test_gits_track_happy_case(mock_var, mock_args):
    """
    Function to test gits track, success case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_track(mock_args)
    assert True == test_result, "Normal case"


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace())
@patch("gits_logging.gits_logger")
def test_gits_track_sad_case(mock_err, mock_args):
    """
    Function to test gits track, failure case
    """
    mock_args = parse_args(mock_args)
    test_result = gits_track(mock_args)
    assert False == test_result


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(file_names=[]))
@patch("subprocess.Popen")
def test_gits_track_happy_case_no_files(mock_var, mock_args):
    """
    Function to test gits track, success case when no files are passed as argument
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_track(mock_args)
    assert True == test_result, "Normal case"