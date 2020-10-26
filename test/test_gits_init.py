import argparse
import sys
import os
import shutil

sys.path.insert(1, os.getcwd())

from gits_init import gits_init
from mock import patch


def remove_extras(path):
    files = os.listdir(path)
    for file in files:
        if "py" in file:
            continue
        try:
            shutil.rmtree(file)
        except:
            os.remove(file)


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(barre=None, template=None, amend=True))
@patch("subprocess.Popen", return_value="anything")
def test_gits_init_normal(mock_var1, mock_args):
    """
    Function to test gits init, success case
    """
    test_result = gits_init(mock_args)
    remove_extras(".")
    assert test_result == True, "Normal init"

@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(barre=True, template=None, amend=True))
@patch("subprocess.Popen", return_value="anything")
def test_gits_init_bare(mock_var1, mock_args):
    """
    Function to test gits init --bare, success case
    """
    test_result = gits_init(mock_args)
    remove_extras(".")
    assert test_result == True, "Bare init"

@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(barre=None, template="test_template", amend=True))
@patch("subprocess.Popen", return_value="anything")
def test_gits_init_template(mock_var1, mock_args):
    """
    Function to test gits init --template, success case
    """
    test_result = gits_init(mock_args)
    remove_extras(".")
    assert test_result == True, "Template init"

