import os
import re


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

    def open(self, filename):
        accepted_ext = {
            ".trc": Trc,
            ".log": Log,
        }
        file_ext = "." + filename.split(".")[-1]
        self.file_obj = accepted_ext.get(file_ext)
        if not self.file_obj:
            raise Exception(f"{filename} is not an accepted file.")
        return self.file_obj(filename, self.path_)

    def listdir(self):
        return os.listdir(self.path_)

    def listcsv(self):
        return [i for i in self.listdir() if i.endswith(".csv")]

    def listxls(self):
        return [i for i in self.listdir() if i.endswith(".xls")]

    def listxlsx(self):
        return [i for i in self.listdir() if i.endswith(".xlsx")]


class TextFileBase:
    def __init__(self, filename, path_):
        self.filename = filename
        self.path_ = path_
        with open(os.path.join(self.path_, self.filename), "r") as file_:
            self.file_ = file_.readlines()

    def __getitem__(self, idx):
        return self.file_[idx]

    def __len__(self):
        return len(self.file_)

    def __repr__(self):
        return f'{__class__.__name__}("{self.path_}\\{self.filename}")'

    @property
    def filename(self):
        return self.filename

    @filename.setter
    def filename(self, filename):
        self.filename = filename

    def readline(self):
        yield from self.file_

    def readlines(self):
        return self.file_

    def find(self, str_, ignore_case=False):
        if not ignore_case:
            for line in self.readline():
                if str_ in line:
                    yield line
        for line in self.readline():
            if str_.lower() in line.lower():
                yield line

    def findall(self, str_, ignore_case=False):
        if not ignore_case:
            return [line for line in self.readline() if str_ in line]
        return [line for line in self.readline() if str_.lower() in line.lower()]

    def findall_re(self, re_pattern, **kwargs):
        return [re.findall(re_pattern, str_, **kwargs) for str_ in self.file_]


class Trc(TextFileBase):
    def __init__(self, trc_file, path_):
        super().__init__(trc_file, path_)
        self.trc_file = trc_file

    def __repr__(self):
        return f'{__class__.__name__}("{self.path_}\\{self.filename}")'


class Log(TextFileBase):
    def __init__(self, log_file, path_):
        super().__init__(log_file, path_)
        self.log_file = log_file

    def __repr__(self):
        return f'{__class__.__name__}("{self.path_}\\{self.filename}")'

    # [TODO] : method to parse .log file (Import, Export) to dict obj
