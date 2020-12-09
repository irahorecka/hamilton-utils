class TrcDict:
    def __init__(self, trc):
        # accepts trc.readlines() (i.e. list of str)
        self.trc_json = self.__to_dict(trc) if not isinstance(trc[0], dict) else trc

    def __call__(self):
        return self.trc_json

    def keep(self, *funcs):
        data=self.trc_json
        for func in funcs:
            data=[d for d in data if func(d)]
        return TrcDict(data)

    def head(self, n):
        return TrcDict([self.trc_json[i] for i in range(n)])

    def tail(self, n):
        return TrcDict([self.trc_json[-i] for i in range(1, n+1)])

    def select(self, *keys):
        return TrcDict([{k: d[k] for k in keys} for d in self.trc_json])

    def __to_dict(self, trc):
        return [self.__get_datetime(line) for line in trc]

    def __get_datetime(self, str_):
        kwargs = {'datetime': str_.split('>')[0]}
        str_=''.join(str_.split('>')[1:])
        return self.__get_calltype(str_, **kwargs)

    def __get_calltype(self, str_, **kwargs):
        kwargs['calltype']=str_.split(':')[0]
        str_=''.join(str_.split(':')[1:])
        return self.__get_callstatus(str_, **kwargs)

    def __get_callstatus(self, str_, **kwargs):
        kwargs['callstatus']=str_.split('-')[0]
        str_=''.join(str_.split('-')[1:])
        return self.__get_callprogress(str_, **kwargs)

    def __get_callprogress(self, str_, **kwargs):
        kwargs['callprogress']=str_.split(';')[0]
        str_=''.join(str_.split(';')[1:])
        return self.__get_extra(str_, **kwargs)

    def __get_extra(self, str_, **kwargs):
        kwargs['extra']=str_
        return kwargs

        

if __name__=='__main__':
    from pprint import pprint
    with open('DaugherPlatePrep with Channels_v2_1_9e15559ebbbf4a5aa09a436939787513_Trace.trc', 'r') as trc:
        trc=trc.read().splitlines()
    converter=TrcDict(trc)
    pprint(converter.select('datetime','callstatus','callprogress','extra').tail(100)())
