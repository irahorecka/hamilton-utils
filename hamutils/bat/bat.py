import os
import subprocess


def admin_rm(path_, file_):
    subprocess.call(
        [
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "admin_cmd.bat"),
            os.path.join(path_, file_),
        ]
    )
