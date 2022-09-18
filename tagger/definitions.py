import os

from tagger.utils import get_file_parent_path


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT_DIR = get_file_parent_path(ROOT_DIR)
