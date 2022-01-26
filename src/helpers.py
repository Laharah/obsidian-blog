import os
from distutils.dir_util import copy_tree
import shutil

from slugify.slugify import slugify
from src import fs

def normalize_path(path: str):
  if path[0] == '/':
    return os.path.realpath(path)
  return path

def traverseBy(key, head, cb):
  if not head: return
  cb(head)
  if type(getattr(head, key)) is list:
    for child in getattr(head, key):
      traverseBy(key, child, cb)

def get_slug(node) -> str:
  file, _ = os.path.splitext(node.filename)
  slug = slugify(fs.basename(file))
  if node.meta.get("slug"):
    slug = node.meta.get("slug")
  return f"{slug}.html"
