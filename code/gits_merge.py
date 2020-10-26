#!/usr/bin/python3

from subprocess import PIPE
import subprocess


def merge_branch(args):
    """
    Function that allows user to merge any branch into current branch
    """
    try:
        merge_cmd = list()
        merge_cmd.append("git")
        merge_cmd.append("merge")
        merge_cmd.append(args.branch_name)
        process1 = subprocess.Popen(merge_cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()
        # print(stdout.decode("UTF-8"))

    except Exception as e:
        print("ERROR: gits merge command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
