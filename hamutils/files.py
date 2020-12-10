from .base import TextFileBase


class Trc(TextFileBase):
    def __init__(self, filepath_):
        super().__init__(filepath_)

    def __repr__(self):
        return f'{__class__.__name__}("{self.filepath_}")'

    def to_dict(self):
        return TrcDict(self.filepath_)


class TrcDict:
    def __init__(self, trc):
        # accepts trc.readlines() (i.e. list of str)
        self.trc_json = self.__to_dict(trc) if not isinstance(trc[0], dict) else trc

    def __call__(self):
        return self.trc_json

    def keep(self, *funcs):
        data = self.trc_json
        for func in funcs:
            data = [d for d in data if func(d)]
        return TrcDict(data)

    def head(self, n):
        return TrcDict([self.trc_json[i] for i in range(n)])

    def tail(self, n):
        return TrcDict([self.trc_json[-i] for i in range(1, n + 1)])

    def select(self, *keys):
        return TrcDict([{k: d[k] for k in keys} for d in self.trc_json])

    def mutate(self, **kwargs):
        data = self.trc_json
        for key, func in kwargs.items():
            for i in range(len(data)):
                data[i][key] = func(data[i])
        return TrcDict(data)

    def sort(self, key, reverse=False):
        return TrcDict(sorted(self.trc_json, key=key, reverse=reverse))

    def __to_dict(self, trc):
        return [self.__get_datetime(line) for line in trc]

    def __get_datetime(self, str_):
        kwargs = {"datetime": str_.split(">")[0]}
        str_ = "".join(str_.split(">")[1:])
        return self.__get_calltype(str_, **kwargs)

    def __get_calltype(self, str_, **kwargs):
        kwargs["calltype"] = str_.split(":")[0]
        str_ = "".join(str_.split(":")[1:])
        return self.__get_callstatus(str_, **kwargs)

    def __get_callstatus(self, str_, **kwargs):
        kwargs["callstatus"] = str_.split("-")[0]
        str_ = "".join(str_.split("-")[1:])
        return self.__get_callprogress(str_, **kwargs)

    def __get_callprogress(self, str_, **kwargs):
        kwargs["callprogress"] = str_.split(";")[0]
        str_ = "".join(str_.split(";")[1:])
        return self.__get_extra(str_, **kwargs)

    def __get_extra(self, str_, **kwargs):
        kwargs["extra"] = str_
        return kwargs


class Log(TextFileBase):
    def __init__(self, filepath_):
        super().__init__(filepath_)

    def __repr__(self):
        return f'{__class__.__name__}("{self.filepath_}")'

    # [TODO] : method to parse .log file (Import, Export) to dict obj
