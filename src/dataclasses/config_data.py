from dataclasses import dataclass, fields
from dotenv.main import dotenv_values


@dataclass
class ConfigData:
    drafts: bool = False
<<<<<<< HEAD
    blog_title: str = "My Blog"
    dest_dir: str = ".build"
    source_dir: str = ".blog"
    posts_dir: str = "Posts"
    pages_dir: str = "Pages"
    layouts_dir: str = ".blog/_layouts"
    assets_dir: str = ".blog/_assets"
    assets_dest_dir: str = ".build/static"
    public_dir: str = "/static"
    default_layout: str = "main"
=======
    blog_title: str = 'My Blog'
    dest_dir: str = '.build'
    source_dir: str = '.blog'
    posts_dir: str = 'Posts'
    pages_dir: str = 'Pages'
    partials_dir: str = ".blog/_partials"
    layouts_dir: str = '.blog/_layouts'
    assets_dir: str = '.blog/_assets'
    assets_dest_dir: str = '.build/static'
    public_dir: str = '/static'
    refresh_delay: int = 40
    default_layout: str = 'main'
>>>>>>> Add support for partials, helpers, and more custom config
    port: int = 4200

    def override(self, config: dict):
        """override config values from a given dict"""
        for k, v in config.items():
            setattr(self, k, v)

    def load_dotenv(self):
        self.override(dotenv_values(".env"))


config = ConfigData()
