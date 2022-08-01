from dataclasses import dataclass
import os
from src.lib import fs
from src.converters import handlebars


@dataclass
class Partial:
    def __init__(self, filename):
        self.filename = filename
        with open(filename) as f:
            hbs_str = f.read()
        self.template_fn = handlebars.create_template_fn(hbs_str)

    @property
    def name(self):
        name = os.path.basename(self.filename)
        return name

    @property
    def fn(self):
        with open(self.filename) as f:
            hbs_str = f.read()
        return handlebars.create_template_fn(hbs_str)

    @staticmethod
    def get_all(partials_dir):
        partials = {}

        for file in fs.get_files_in_dir(partials_dir):
            partial = Partial(file)
            partials[partial.name] = partial

        return partials

    # def render(self, ctx):
    #     return self.fn(ctx)
