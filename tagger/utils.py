import json
import pathlib
from typing import Union
from datetime import datetime


def get_file_parent_path(file_path):
    path = pathlib.Path(file_path)
    return path.parent


def folder_exists(folder_path: Union[pathlib.Path, str]) -> bool:
    return pathlib.Path(folder_path).is_dir()


def file_exists(file_path: Union[pathlib.Path, str]) -> bool:
    return pathlib.Path(file_path).is_file()


def create_init_config(tagger_path: Union[pathlib.Path, str]):
    from tagger.definitions import TAGGER_META_FILENAME
    timestamp = datetime.strftime(datetime.now(), "%m/%d/%Y--%H:%M:%S")
    init_config = {
        "creation_timestamp": timestamp
    }
    with open(f"{tagger_path}/{TAGGER_META_FILENAME}", "w") as infile:
        json.dump(init_config, infile)


def create_directory(directory_to_create: Union[pathlib.Path, str]):
    if not isinstance(directory_to_create, pathlib.Path):
        pathlib.Path(directory_to_create).mkdir(parents=True, exist_ok=True)
