#!/usr/bin/python3

import os
import sys
from subprocess import Popen, PIPE


def create_branch(args):
    """
    Function that creates a new local branch
    from local master after updating local master
    from remote master
    """
    try:
        # checkout master first
        checkout_master = list()
        checkout_master.append("git")
        checkout_master.append("checkout")
        checkout_master.append("master")
        print(checkout_master)
        process1 = Popen(checkout_master, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()

        # if any local changes are there, it will error out here
        if stderr:
            print(stderr)
            return False

        # update with remote
        update_master = list()
        update_master.append("git")
        update_master.append("pull")
        print(update_master)
        process2 = Popen(update_master, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process2.communicate()

        # in case of merge conflicts
        if stderr:
            print(stderr)
            return False

        else:
            # checkout new branch
            if not args.b:
                print("Name of new branch not provided. Use -b branchName")
                return False
            checkout_feature = list()
            checkout_feature.append("git")
            checkout_feature.append("checkout")
            checkout_feature.append("-b")
            checkout_feature.append(args.b)
            print(checkout_feature)
            process3 = Popen(checkout_feature, stdout=PIPE, stderr=PIPE)
            stdout, stderr = process3.communicate()

    except Exception as e:
        print("ERROR: gits create command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
