import os
import subprocess


class HamiltonBase:
    def __init__(self, path_):
        self.path_ = path_

    def __repr__(self):
        return f'{__class__.__name__}("{self.path_}")'

    @property
    def path(self):
        return self.path_

    @path.setter
    def path(self, path_):
        self.path_ = path_

    def rm_all(self, endswith_):
        subprocess.call(["./bat/admin_cmd.bat", ""])
        for file_ in self.listdir():
            if file_.endswith(endswith_):
                try:
                    os.remove(os.path.join(self.path_, file_))
                except PermissionError as e:
                    print(e)

    def listdir(self):
        return os.listdir(self.path_)

    def listcsv(self):
        return [i for i in self.listdir() if i.endswith(".csv")]

    def listxls(self):
        return [i for i in self.listdir() if i.endswith(".xls")]

    def listxlsx(self):
        return [i for i in self.listdir() if i.endswith(".xlsx")]


class FileBase:
    def __init__(self, filename, path_):
        self.filename = filename
        self.path_ = path_
        with open(os.path.join(self.path_, self.filename), "r") as file_:
            self.file_ = file_.readlines()

    def readlines(self):
        return self.file_

    def find(self, str_):
        return [line for line in self.readlines() if str_ in line]
        # for line in self.readlines():
        #     if str_ in line:
        #         yield line

    def find_regex(self, re_pattern):
        pass


class Trc(FileBase):
    def __init__(self, trc_file, path_):
        super().__init__(trc_file, path_)
        self.trc_file = trc_file


class Log(FileBase):
    def __init__(self, log_file, path_):
        super().__init__(log_file, path_)
        self.log_file = log_file

    def to_dict(self):
        pass
