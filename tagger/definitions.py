import os

from tagger.utils import get_file_parent_path


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT_DIR = get_file_parent_path(ROOT_DIR)
TAGGER_ROOT_DIR = ".tag"
TAGGER_META_FILENAME = "config.json"
DEFAULT_DB_NAME = "tagr.db"
