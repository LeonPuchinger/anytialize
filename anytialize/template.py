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
        path = next(self.find_templates(name, searchpaths))
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

    @staticmethod
    def find_templates(name, paths):
        templates = 0
        for path in paths:
            for dirpath, _, files in os.walk(path):
                for file in files:
                    filename, fileext = os.path.splitext(file)
                    dirname = os.path.basename(dirpath)
                    if fileext == ".yaml" and filename == dirname:
                        if filename == name:
                            yield os.path.join(dirpath, file)
                        if name == "":
                            yield filename
                            templates += 1
        if templates == 0:
            raise AnytException(f"ERROR: no template found by the name \"{name}\"")

    def _parse(self):
        template = yaml.load(self.template, Loader=yaml.FullLoader)
        if template == None:
            raise AnytException(f"ERROR: template empty")
        for action in template:
            if action["type"] == "cp":
                copypaste(action["src"], action["dest"])
            if action["type"] == "shell":
                shell(action["command"], action["args"])
