#!/usr/bin/python3

import os
import gits_logging
from pathlib import Path


def gits_set_func(args):
    """
    Function that is used to set important
    environment variables
    """
    try:
        if args.parent:
            parent_name = args.parent.strip()
            user_home_dir = str(Path.home())
            gits_parent_file = os.path.join(user_home_dir, ".gits", "parent")
            with open(gits_parent_file, "w") as fp:
                fp.write(parent_name)
            gits_logging.gits_logger.info("Parent : {} ".format(args.parent))
        else:
            gits_logging.gits_logger.info("Parent argument was not passed ")
    except Exception as e:
        print("ERROR: gits set command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
