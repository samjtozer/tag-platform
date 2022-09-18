import json
import pathlib
from typing import Union
from datetime import datetime
from uuid import uuid4
from glob import glob

from tagger.models.utils import _add_project_item


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


def create_project(project_name: str, project_description: str = ""):
    from tagger.definitions import REPO_ROOT_DIR, TAGGER_ROOT_DIR
    local_project_id = max([
        int(pathlib.Path(dir).name) for dir in glob(f"{REPO_ROOT_DIR}/{TAGGER_ROOT_DIR}/projects/*")
    ] + [-1]) + 1
    new_project_dir = f"{REPO_ROOT_DIR}/{TAGGER_ROOT_DIR}/projects/{local_project_id}"
    project_id = str(uuid4())
    project_config = {
        "project_id": project_id,
        "project_name": project_name,
        "project_description": project_description,
    }
    create_directory(new_project_dir)
    with open(f"{new_project_dir}/meta.json", "w") as infile:
        json.dump(project_config, infile)
    # Also add a new record to the project table
    _add_project_item(
        project_id=project_id,
        project_name=project_name,
        project_description=project_description,
        folder_pointer=local_project_id
    )
