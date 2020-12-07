from .base import TextFileBase


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
