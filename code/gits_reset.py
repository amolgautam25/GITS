import subprocess
from subprocess import PIPE


def gits_reset(args):
    # print(args)
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
