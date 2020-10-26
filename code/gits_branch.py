#!/usr/bin/python3

from subprocess import Popen, PIPE


def gits_branch(args):
    """
    Function that allows users to show difference from last commit
    """
    try:
        diff_cmd = list()
        diff_cmd.append("git")
        diff_cmd.append("branch")
        process1 = Popen(diff_cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()
        print(stdout.decode("UTF-8"))

    except Exception as e:
        print("ERROR: gits branch command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
