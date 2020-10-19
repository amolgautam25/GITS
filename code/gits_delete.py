import subprocess
from subprocess import PIPE


def gits_delete(args):
    """
    Please use this functionality with caution since there would be no going back from this.
    This function will delete a commit from the remote branch.
    This functionality is useful when you have commited a mistake to the remote repo and do not
    want it be visible in your commit history.
    """
    print("Hello from GITS command line tools- GITS reset")
    try:
        process1 = subprocess.Popen(['git', 'checkout', args.branch], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()
        process2 = subprocess.Popen(['git', 'reset', '--hard', "HEAD~"+str(args.count)], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process2.communicate()
        process3 = subprocess.Popen(['git', 'push', '--force'], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process3.communicate()
        print('Last '+args.count+' commits have been deleted')
    except Exception as e:
        print("ERROR: gits reset command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False
    return True
