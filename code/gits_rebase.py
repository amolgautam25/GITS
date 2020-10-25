import subprocess
from subprocess import PIPE


def gits_rebase(args):
    """This is a highly simplified version of git rebase command.
    This interactive command asks for the branch that you want to rebase and automatically rebases it off master.
    This is the most common scenario. The original GIT rebase command is a little un-intuitive and there is always a
    confusion , about the source branch and the destination branch.
"""
    try:
        print("Is the rebase on current branch?")
        inp = input("[yes/no][y/n]")
        if inp.lower() == "yes" or inp.lower() == "y":
            process1 = subprocess.Popen(['git', 'rebase', 'master'], stdout=PIPE, stderr=PIPE)
            stdout, stderr = process1.communicate()
            print(stdout)
        else:
            inp2 = input("Enter the name of the branch you want to rebase: ")
            # print(inp2)
            process2 = subprocess.Popen(['git', 'checkout', inp2, 'git', 'rebase', 'master'], stdout=PIPE, stderr=PIPE)
            stdout, stderr = process2.communicate()
            print(stdout)
    except Exception as e:
        print("ERROR: gits reset command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False
    return True
