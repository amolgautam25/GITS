import logging
import os
import sys
import time
from pathlib import Path
from logging.handlers import TimedRotatingFileHandler

gits_logger = None

def init_gits_logger():
    """
    Function that initializes gits logger and creates a
    handler to be used consequently
    """
    try:
        global gits_logger
        # format the log entries
        formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
        
        user_home_dir = str(Path.home())
        gits_logs_dir = os.path.join(user_home_dir, ".gits", "logs")
        
        #checking if logs directory exist or not
        if os.path.isdir(gits_logs_dir):
            #do nothing
            pass
        else:
            print("gits project not initialised, run project_init.sh "\
                  "script from configurations to initialize the project")
            sys.exit(1)
        
        gits_logs_filename = os.path.join(gits_logs_dir, "gits.log")
        handler = TimedRotatingFileHandler(gits_logs_filename, 
                                           when='midnight',
                                           backupCount=10)
        
        handler.setFormatter(formatter)
        gits_logger = logging.getLogger(__name__)
        gits_logger.addHandler(handler)
        gits_logger.setLevel(logging.DEBUG)
        return True
    except Exception as e:
        print("ERROR: Caught exception {}".format(str(e)))
        return False

