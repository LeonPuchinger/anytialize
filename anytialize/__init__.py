from .template import Template
from .config import *
#exports
from .util import AnytException

def run_template(template, args):
    config = config_default()
    template = Template(template, config["template-path"])
    template.run(args)

def list_templates():
    config = config_default()
    templates = Template.find_all_templates(config["template-path"])
    for t in templates:
        print(t)
