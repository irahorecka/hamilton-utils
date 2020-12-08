import os
import re


class HamiltonBase:
    accepted_file_ext = {}

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

    def listdir(self):
        return os.listdir(self.path_)

    def listcsv(self):
        return [i for i in self.listdir() if i.endswith(".csv")]

    def listini(self):
        return [i for i in self.listdir() if i.endswith(".ini")]

    def listxls(self):
        return [i for i in self.listdir() if i.endswith(".xls")]

    def listxlsx(self):
        return [i for i in self.listdir() if i.endswith(".xlsx")]


class TextFileBase:
    def __init__(self, filepath_, mode):
        self.filepath_ = filepath_
        self.file_ = open(self.filepath_, mode)

    def __enter__(self):
        return self.file_

    def __exit__(self, exc_type, exc_value, traceback):
        self.file_.close()

    def __repr__(self):
        return f'{__class__.__name__}("{self.filepath_}")'

    @property
    def path(self):
        return self.filepath_

    def find(self, str_, ignore_case=False):
        if not ignore_case:
            for line in self.file_.readlines():
                if str_ in line:
                    yield line
        for line in self.file_.readlines():
            if str_.lower() in line.lower():
                yield line

    def findall(self, str_, ignore_case=False):
        if not ignore_case:
            return [line for line in self.file_.readlines() if str_ in line]
        return [line for line in self.file_.readlines() if str_.lower() in line.lower()]

    def findall_re(self, re_pattern, **kwargs):
        return [
            re.findall(re_pattern, str_, **kwargs) for str_ in self.file_.readlines()
        ]
