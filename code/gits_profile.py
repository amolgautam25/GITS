import os
import sys
import subprocess
import re
from subprocess import Popen, PIPE


def gits_set_profile(args):
    """
    Function that prints hello message
    to user console
    """
    # print(args.email)
    # print("Hello from GITS Commandline Tools-Profile")
    try:
        check_val = check(args.email)
        # print(check_val)
        if check_val == True:
            profile_unset_email_command = list()
            profile_unset_email_command.append("git")
            profile_unset_email_command.append("config")
            profile_unset_email_command.append("--global")
            profile_unset_email_command.append("--unset")
            profile_unset_email_command.append("user.email")

            profile_unset_name_command = list()
            profile_unset_name_command.append("git")
            profile_unset_name_command.append("config")
            profile_unset_name_command.append("--global")
            profile_unset_name_command.append("--unset")
            profile_unset_name_command.append("user.name")

            process = subprocess.Popen(profile_unset_email_command, stdout=PIPE, stderr=PIPE)
            stdout, stderr = process.communicate()

            process1 = subprocess.Popen(profile_unset_name_command, stdout=PIPE, stderr=PIPE)
            stdout, stderr = process1.communicate()

            # check regex
            profile_set_name_command = list()
            profile_set_name_command.append("git")
            profile_set_name_command.append("config")
            profile_set_name_command.append("--global")
            profile_set_name_command.append("user.name")
            profile_set_name_command.append(args.name)
            # print(cmd)
            process2 = subprocess.Popen(profile_set_name_command, stdout=PIPE, stderr=PIPE)
            stdout, stderr = process2.communicate()

            profile_set_email_command = list()
            profile_set_email_command.append("git")
            profile_set_email_command.append("config")
            profile_set_email_command.append("--global")
            profile_set_email_command.append("user.email")
            profile_set_email_command.append(args.email)

            process3 = subprocess.Popen(profile_set_email_command, stdout=PIPE, stderr=PIPE)
            stdout, stderr = process3.communicate()

            profile_verify_name_command = list()
            profile_verify_name_command.append("git")
            profile_verify_name_command.append("config")
            profile_verify_name_command.append("--list")

            profile_verify_name = list()
            profile_verify_name.append("grep")
            profile_verify_name.append('user.name')

            process4 = subprocess.Popen(profile_verify_name_command, stdout=PIPE, stderr=PIPE)
            process41 = subprocess.Popen(profile_verify_name, stdin=process4.stdout,
                                     stdout=PIPE, stderr=PIPE)
            stdout, stderr = process41.communicate()

            print(stdout)

            profile_verify_email_command = list()
            profile_verify_email_command.append("git")
            profile_verify_email_command.append("config")
            profile_verify_email_command.append("--list")

            profile_verify_email = list()
            profile_verify_email.append("grep")
            profile_verify_email.append("user.email")

            process5 = subprocess.Popen(profile_verify_email_command, stdout=PIPE, stderr=PIPE)
            process51 = subprocess.Popen(profile_verify_email, stdin=process5.stdout,
                                         stdout=PIPE, stderr=PIPE)
            stdout, stderr = process51.communicate()

            print(stdout)

        else:
            print("Enter a valid email id")

    except Exception as e:
        print("ERROR: gits profile command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True


# Define a function for
# for validating an Email
def check(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    # for custom mails use: '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

    # pass the regular expression
    # and the string in search() method
    if (re.search(regex, email)):
        return True
    else:
        return False




