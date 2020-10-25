import argparse
import sys
import os

sys.path.insert(1, os.getcwd())

from gits_init import gits_init
from mock import patch

@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(barre=None, template=None, amend=True))
@patch("subprocess.Popen", return_value="anything")
def test_gits_init_normal(mock_var1, mock_args):
    """
    Function to test gits init, success case
    """
    test_result = gits_init(mock_args)
    assert test_result == True, "Normal init"

@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(barre=True, template=None, amend=True))
@patch("subprocess.Popen", return_value="anything")
def test_gits_init_bare(mock_var1, mock_args):
    """
    Function to test gits init --bare, success case
    """
    test_result = gits_init(mock_args)
    assert test_result == True, "Bare init"

@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(barre=None, template="test_template", amend=True))
@patch("subprocess.Popen", return_value="anything")
def test_gits_init_template(mock_var1, mock_args):
    """
    Function to test gits init --template, success case
    """
    test_result = gits_init(mock_args)
    assert test_result == True, "Template init"

