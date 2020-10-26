import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from helper import get_current_branch
from mock import patch, Mock


@patch("subprocess.Popen")
def test_get_current_branch_happy_case(mock_var):
    """
    Function to test fetching current branch, success case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output'.encode('UTF-8'), 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    test_result = get_current_branch()
    assert "output" == test_result, "Normal case"


@patch("subprocess.Popen")
def test_get_current_branch_sad_case(mock_var):
    """
    Function to test fetching current branch, success case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    test_result = get_current_branch()
    assert None == test_result


@patch("subprocess.Popen")
def test_get_trunk_branch_happy_case_master_branch(mock_var):
    """
    Function to test fetching main branch, success case when trunk branch='master'
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('master'.encode('UTF-8'), 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    test_result = get_current_branch()
    assert "master" == test_result, "Normal case"


@patch("subprocess.Popen")
def test_get_trunk_branch_happy_case_main_branch(mock_var):
    """
    Function to test fetching main branch, success case when trunk branch='main'
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('main'.encode('UTF-8'), 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    test_result = get_current_branch()
    assert "main" == test_result, "Normal case"


@patch("subprocess.Popen")
def test_get_trunk_branch_happy_case_other_branch(mock_var):
    """
    Function to test fetching main branch, success case when trunk branch is any other branch
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('branch'.encode('UTF-8'), 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    test_result = get_current_branch()
    assert "branch" == test_result, "Normal case"


@patch("subprocess.Popen")
def test_get_trunk_branch_sad_case(mock_var):
    """
    Function to test fetching main branch, failure case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('branch', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    test_result = get_current_branch()
    assert None == test_result


