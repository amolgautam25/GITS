import subprocess
from subprocess import PIPE


def gits_reset(args):
    """'Reset' intuitively means a HARD reset. This functionality does a HARD reset on your branch, and makes it even with the remote branch. This aims to simplify the confusion between HARD and the SOFT reset."""
    print("Hello from GITS command line tools- GITS reset")
    try:
        process1 = subprocess.Popen(['git', 'checkout', args.branch], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()
        # print(stdout)
        process2 = subprocess.Popen(['git', 'reset', '--hard', 'origin', args.branch], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process2.communicate()
        # print(stdout)
    except Exception as e:
        print("ERROR: gits reset command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False
    return True
