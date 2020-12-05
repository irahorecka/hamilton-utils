from .base import HamiltonBase

class LogFile(HamiltonBase):
    def __init__(self):
        super().__init__('logfile')

    def __repr__(self):
        return f'LogFile("{self.yml_key}")'
        
    def rm_ldf(self):
        self.rm_('.ldf')

    def rm_mdf(self):
        self.rm_('.mdf')

    def open_trc(self, filename, **kwargs):
        kwargs['endswith']='.trc'
        trc=self.open_(filename, **kwargs)
        return trc

    def open_log(self, filename, **kwargs):
        kwargs['endswith']='.log'
        trc=self.open_(filename, **kwargs)
        return trc
