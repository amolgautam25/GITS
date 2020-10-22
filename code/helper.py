#!/usr/bin/python3

from subprocess import Popen, PIPE


def get_current_branch():
    """
    This function returns current checked out branch.
    """
    subprocess_command = list()
    subprocess_command.append("git")
    subprocess_command.append("rev-parse")
    subprocess_command.append("--abbrev-ref")
    subprocess_command.append("HEAD")
    process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    branch = stdout.decode('UTF-8')

    return branch.rstrip()
