import os
from .base import HamiltonBase
from .bat import admin_rm
from .files import Trc, Log


class LogFile(HamiltonBase):
    accepted_file_ext = {
        ".trc": Trc,
        ".log": Log,
    }

    def __init__(self):
        self.path_ = "C:\\Program Files (x86)\\HAMILTON\\LogFiles"
        super().__init__(self.path_)

    def __repr__(self):
        return f'{__class__.__name__}("{self.path_}")'

    def open(self, filename_, mode):
        file_ext = "." + filename_.split(".")[-1]
        self.file_obj = self.accepted_file_ext.get(file_ext)
        if not self.file_obj:
            raise Exception(f"{filename_} is not an accepted file.")
        filepath_ = os.path.join(self.path_, filename_)

        return self.file_obj(filepath_, mode)

    def rm_ldf(self):
        admin_rm(self.path_, "*.ldf")

    def rm_mdf(self):
        admin_rm(self.path_, "*.mdf")

    def listldf(self):
        return [i for i in self.listdir() if i.endswith(".ldf")]

    def listlog(self):
        return [i for i in self.listdir() if i.endswith(".log")]

    def listmdf(self):
        return [i for i in self.listdir() if i.endswith(".mdf")]

    def listtrc(self):
        return [i for i in self.listdir() if i.endswith(".trc")]


class Methods(HamiltonBase):
    def __init__(self, path_):
        if not self.path_:
            self.path_ = "C:\\Program Files (x86)\\HAMILTON\\Methods"
        else:
            self.path_ = path_
        super().__init__(self.path_)

    def __repr__(self):
        return f'{__class__.__name__}("{self.path_}")'

    def listhsl(self):
        return [i for i in self.listdir() if i.endswith(".hsl")]

    def listlay(self):
        return [i for i in self.listdir() if i.endswith(".lay")]

    def listmed(self):
        return [i for i in self.listdir() if i.endswith(".med")]

    def listres(self):
        return [i for i in self.listdir() if i.endswith(".res")]


class Library(HamiltonBase):
    def __init__(self, path_):
        if not self.path_:
            self.path_ = "C:\\Program Files (x86)\\HAMILTON\\Library"
        else:
            self.path_ = path_
        super().__init__(self.path_)

    def __repr__(self):
        return f'{__class__.__name__}("{self.path_}")'


class Labware(HamiltonBase):
    def __init__(self, path_):
        if not self.path_:
            self.path_ = "C:\\Program Files (x86)\\HAMILTON\\Labware"
        else:
            self.path_ = path_
        super().__init__(self.path_)

    def __repr__(self):
        return f'{__class__.__name__}("{self.path_}")'


class SupportingFiles(HamiltonBase):
    def __init__(self, path_):
        if not self.path_:
            self.path_ = "C:\\Program Files (x86)\\HAMILTON\\SupportingFiles"
        else:
            self.path_ = path_
        super().__init__(self.path_)

    def __repr__(self):
        return f'{__class__.__name__}("{self.path_}")'
