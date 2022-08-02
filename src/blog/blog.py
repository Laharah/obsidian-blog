from src.lib import fs
from src.blog.layout import Layout
from src.blog.partial import Partial
from datetime import datetime
from src.dataclasses.config_data import ConfigData


class Blog:
    """Handles blog related setup, like getting layouts, etc"""

    def __init__(self, config: ConfigData):
        self.config = config
        self.layouts = self.load_layouts()
        self.partials = self.load_partials()
        self.helpers = self.load_helpers()

    def load_layouts(self):
        return Layout.get_all(self.config.layouts_dir)

    def load_partials(self):
        return Partial.get_all(self.config.partials_dir)

    def load_helpers(self):
        helpers = {}

        def _ifeq(this, a, b):
            return a == b

        helpers["ifeq"] = _ifeq

        def _neq(this, a, b):
            return a != b

        helpers["ifneq"] = _neq

        def _date_format(this, d:datetime, format:str):
            return d.strftime(format)

        helpers["dateformat"] = _date_format

        return helpers
