import subprocess
from subprocess import PIPE
from helper import get_current_branch

def gits_push(args):
    try:
        untracked_file_check_status = ["git", "status", "--porcelain"]
        process0 = subprocess.Popen(untracked_file_check_status,
                                    stdout=PIPE, stderr=PIPE)

        stdout, stderr = process1.communicate()
        print(stdout.decode("utf-8"))

        if stdout != b'':
            print("Note: Please commit uncommited changes")
            exit()

        curr_branch = get_current_branch()

        print("Pulling changes from Upstream source branch and rebasing it")
        pull_rebase = ["git", "pull", "--rebase", "origin", curr_branch]
        process1 = subprocess.Popen(pull_rebase, stdout=PIPE, stderr=PIPE)
        
        stdout, stderr = process1.communicate()
        print(stdout.decode("utf-8"))

        print("Pushing local commits")
        push_commits = ["git","push", "origin", curr_branch]
        process2 = subprocess.Popen(push_commits, stdout=PIPE, stderr=PIPE)

        stdout, stderr = process2.communicate()
        print(stdout.decode("utf-8"))
    
    except Exception as e:
        print("ERROR: gits push command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True


