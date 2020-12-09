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

    def listini(self):
        return [i for i in self.listdir() if i.endswith(".ini")]

    def listxls(self):
        return [i for i in self.listdir() if i.endswith(".xls")]

    def listxlsx(self):
        return [i for i in self.listdir() if i.endswith(".xlsx")]


class TextFileBase:
    def __init__(self, filepath_):
        self.filepath_ = filepath_
        with open(self.filepath_, "r") as file_:
            self.file_ = file_.readlines()

    def __repr__(self):
        return f'{__class__.__name__}("{self.filepath_}")'

    @property
    def path(self):
        return self.filepath_

    def find(self, str_, ignore_case=False):
        yield from self.findall(str_, ignore_case)

    def findall(self, str_, ignore_case=False):
        if not ignore_case:
            return [line for line in self.file_ if str_ in line]
        return [line for line in self.file_ if str_.lower() in line.lower()]

    def find_re(self, re_pattern, **kwargs):
        yield from self.findall_re(re_pattern, **kwargs)

    def findall_re(self, re_pattern, **kwargs):
        return [re.findall(re_pattern, str_, **kwargs) for str_ in self.file_]
