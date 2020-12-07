from .base import HamiltonBase
from .bat import admin_rm


class LogFile(HamiltonBase):
    def __init__(self):
        self.path_ = "C:\\Program Files (x86)\\HAMILTON\\LogFiles"
        super().__init__(self.path_)

    def __repr__(self):
        return f'{__class__.__name__}("{self.path_}")'

    def rm_ldf(self):
        admin_rm(self.path_, "*.ldf")

    def rm_mdf(self):
        admin_rm(self.path_, "*.mdf")

    def listtrc(self):
        return [i for i in self.listdir() if i.endswith(".trc")]

    def listlog(self):
        return [i for i in self.listdir() if i.endswith(".log")]

    def listini(self):
        return [i for i in self.listdir() if i.endswith(".ini")]

    def listldf(self):
        return [i for i in self.listdir() if i.endswith(".ldf")]

    def listmdf(self):
        return [i for i in self.listdir() if i.endswith(".mdf")]


class Methods(HamiltonBase):
    def __init__(self, path_):
        if not self.path_:
            self.path_ = "C:\\Program Files (x86)\\HAMILTON\\Methods"
        else:
            self.path_ = path_
        super().__init__(self.path_)

    def __repr__(self):
        return f'{__class__.__name__}("{self.path_}")'


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
