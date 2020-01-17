import yaml
import os
from .util import CONFIG_FILE_EXT

_valid_keys = [
    "template-path",
]

def _valid_config(config):
    valid = {}
    for key in config:
        if key in _valid_keys:
            valid[key] = config[key]
    return valid

def config_from_file(file):
    conf = yaml.load(file, Loader=yaml.FullLoader)
    if "anyt-config" not in conf:
        print("anyt-config not found in file")
        return
    return _valid_config(conf["anyt-config"])
    
def config_from_path(path):
    with open(path, "r") as f:
        return config_from_file(f)

def config_default():
    user = os.path.expanduser("~")
    return config_from_path(f"{user}/.anyt/config.{CONFIG_FILE_EXT}")