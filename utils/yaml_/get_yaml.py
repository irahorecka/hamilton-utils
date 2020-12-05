import yaml

def get_environ(key):
    with open("environ.yml") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data[key]