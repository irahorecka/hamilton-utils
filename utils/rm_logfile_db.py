"""This script cycles through all files in the LogFiles folder and tries
to delete any that end with "HamiltonVectorDB.mdf". It will not work
on the most recent file if it is currently open and in use.

For use in Hamilton:
    You cannot call log_db_cleaner through the Hamilton shell command
    if __name__ == "__main__". Call log_db_cleaner in the global scope.
"""

import os
from yaml_ import get_environ

LOGDIR = get_environ('logfile')


def log_db_cleaner(log_db_dir):
    for file_ in os.listdir(log_db_dir):
        if file_.endswith(".mdf") or file_.endswith(".ldf"):
            try:
                os.remove(os.path.join(log_db_dir, file_))
                print(f"Removed: {file_}")
            except PermissionError:
                pass


log_db_cleaner(LOGDIR)
