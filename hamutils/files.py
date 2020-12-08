from .base import TextFileBase


class Trc(TextFileBase):
    def __init__(self, filepath_, mode):
        super().__init__(filepath_, mode)

    def __repr__(self):
        return f'{__class__.__name__}("{self.filepath_}")'


class Log(TextFileBase):
    def __init__(self, filepath_, mode):
        super().__init__(filepath_, mode)

    def __repr__(self):
        return f'{__class__.__name__}("{self.filepath_}")'

    # [TODO] : method to parse .log file (Import, Export) to dict obj
