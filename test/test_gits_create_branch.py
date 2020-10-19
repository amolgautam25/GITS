import argparse
import gits_create_branch
from mock import patch, Mock


@patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace(b="branch name"))
@patch("subprocess.Popen")
def test_git_create_branch_happy_path(mock_popen, mock_args):
    """
    Function to test gits_create_branch, success case
    """
    test_result = gits_create_branch.create_branch(mock_args)
    assert test_result == True
