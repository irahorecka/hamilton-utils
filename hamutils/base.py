import os
import yaml


class HamiltonBase():
    def __init__(self, yml_key):
        self.yml_key=yml_key
        self.set_environ()

    def __repr__(self):
        return f'HamiltonBase("{self.yml_key}")'

    def rm_(self, endswith):
        for file_ in self.listdir():
            if file_.endswith(endswith):
                try:
                    print(os.path.join(self.path_, file_))
                    os.remove(os.path.join(self.path_, file_))
                except PermissionError as e:
                    print(e)

    def open_(self, filename, **kwargs):
        mode=kwargs['mode']
        endswith=kwargs['endswith']
        if not filename.endswith(endswith):
            raise Exception(f'Woah, this is not a {endswith} file.')
        with open(os.path.join(self.path_, filename), mode) as file_:
            return file_.read()

    @property
    def path(self):
        return self.path_

    @path.setter
    def path(self, path_):
        self.path_ = path_

    @property
    def path_key(self):
        return self.yml_key

    @path_key.setter
    def path_key(self, yml_key):
        self.yml_key=yml_key
        self.set_environ()

    def listdir(self):
        return os.listdir(self.path_)

    def set_environ(self):
        with open("environ.yml") as f:
            data = yaml.load(f, Loader=yaml.FullLoader) 
            self.path_=data[self.yml_key]

