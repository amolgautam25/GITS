import argparse
import sys
import os

sys.path.insert(1, os.getcwd())

from gits_undo import gits_undo
from mock import patch


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(file_names="test_file_names"))
@patch("subprocess.Popen", return_value="anything")
def test_gits_add_func_1(mock_var1, mock_args):
    """
    Function to test gits_add, success case
    """
    test_result = gits_undo(mock_args)
    assert True == test_result, "Normal case"
