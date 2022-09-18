import pathlib
from typing import Union


def get_file_parent_path(file_path):
    path = pathlib.Path(file_path)
    return path.parent


def file_exists(file_path: Union[pathlib.Path, str]) -> bool:
    return pathlib.Path(file_path).is_file()
