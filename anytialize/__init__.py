from .template import Template
from .config import config_from_path
#exports
from .util import AnytException

def execute(template, args):
    config = config_from_path("/home/leon/.anyt/templates/config.yaml")
    template = Template(template, config["template-path"])
    template.run(args)