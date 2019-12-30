import os
import yaml
from .actions import *
from .util import AnytException

_valid_keys = {
        "cp": [
            "src",
            "dest",
        ],
        "shell": [
            "command",
            "args",
        ]
    }

class Template:
    def __init__(self, name, searchpaths):
        path = self._find_first_path(name, searchpaths)
        with open(path, "r") as template:
            self.template = template.read()

    def run(self, args=[]):
        if self.template is None:
            print("ERROR: template empty")
            return
        self._preprocess(args)
        self._parse()

    def _preprocess(self, args):
        for num, arg in enumerate(args):
            self.template = self.template.replace(f"$input{num}", arg)

    def _find_first_path(self, name, paths):
        for path in paths:
            for dirpath, _, files in os.walk(path):
                for file in files:
                    if file == name + ".yaml":
                        return os.path.join(dirpath, file)
        raise AnytException(f"ERROR: no template found by the name \"{name}\"")

    def _parse(self):
        template = yaml.load(self.template, Loader=yaml.FullLoader)
        for action in template:
            if action["type"] == "cp":
                copypaste(action["src"], action["dest"])
            if action["type"] == "shell":
                shell(action["command"], action["args"])
