#!/usr/bin/python3

from subprocess import Popen, PIPE


def get_current_branch():
    """
    This function returns current checked out branch.
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("rev-parse")
        subprocess_command.append("--abbrev-ref")
        subprocess_command.append("HEAD")
        process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        branch = stdout.decode('UTF-8')

        return branch.rstrip()

    except:
        print("error occured while getting current branch name!")
        return None

def get_trunk_branch_name():
    """
    This function returns the name of the trunk branch for the project
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("branch")
        process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        all_branches = stdout.decode('UTF-8')
        list_of_branch_names = all_branches.split()
        list_of_branch_names.remove('*')
        if "master" in list_of_branch_names:
            return "master"
        elif "main" in list_of_branch_names:
            return "main"
        else:
            return list_of_branch_names[0]
        return None
    except:
        print("error occured while getting trunk branch name!")
        return None