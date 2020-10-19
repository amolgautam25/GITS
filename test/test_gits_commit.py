import argparse
import os
import sys

os.chdir("../code")
sys.path.insert(1, os.getcwd())

from gits_commit import gits_commit_func
from mock import patch


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(m="test_commit", amend=True))
@patch("subprocess.Popen", return_value="anything")
def test_gits_commit_func_1(mock_var1, mock_args):
    """
    Function to test gits_add, success case
    """
    test_result = gits_commit_func(mock_args)
    assert True == test_result, "Normal case"
