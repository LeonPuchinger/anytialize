import os
import yaml
from .actions import *
from .util import AnytException, CONFIG_FILE_EXT

_valid_keys = {
        "mkdir": [
            "name",
        ],
        "rm": [
            "name"
        ],
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
        self.path, self.name = self._find_first_template(name, searchpaths)
        with open(f"{self.path}/{self.name}.{CONFIG_FILE_EXT}", "r") as template:
            self.template = template.read()

    def run(self, args=[]):
        if self.template is None:
            print("ERROR: template empty")
            return
        self._preprocess(args)
        self._parse()

    def _preprocess(self, args):
        for num, arg in enumerate(args):
            self.template = self.template.replace(f"$input{num}", arg) #inputs
        self.template = self.template.replace("$tp", f"{self.path}") #template path
        self.template = self.template.replace("$cwd", f"{os.getcwd()}") #current working directory

    @staticmethod
    def _loop_templates(paths):
        for path in paths:
            for dirpath, _, files in os.walk(path):
                for file in files:
                    filename, fileext = os.path.splitext(file)
                    dirname = os.path.basename(dirpath)
                    if fileext == f".{CONFIG_FILE_EXT}" and filename == dirname:
                        yield (dirpath, filename)

    @staticmethod
    def _find_first_template(name, paths):
        for tpath, tname in Template._loop_templates(paths):
            if name == tname:
                return (tpath, tname)
        raise AnytException(f"ERROR: no template found by the name \"{name}\"")
        
    @staticmethod
    def find_all_templates(paths):
        templates = 0
        for tpath, tname in Template._loop_templates(paths):
            yield tname
            templates += 1
        if templates == 0:
            raise AnytException(f"WARNING: no templates found")

    def _parse(self):
        template = yaml.load(self.template, Loader=yaml.FullLoader)
        if template == None:
            raise AnytException(f"ERROR: template empty")
        for action in template:
            if action["type"] == "mkdir":
                mkdir(action["name"])
            if action["type"] == "rm":
                rm(action["name"], action["recursive"])
            if action["type"] == "cp":
                copypaste(action["src"], action["dest"])
            if action["type"] == "shell":
                shell(action["command"], action["args"])
