import json
import pathlib
from glob import glob
from uuid import uuid4

from tagger.utils import create_directory
from tagger.models.utils import _add_project_item


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
    create_directory(f"{new_project_dir}/tasks")
    with open(f"{new_project_dir}/meta.json", "w") as infile:
        json.dump(project_config, infile)
    # Also add a new record to the project table
    _add_project_item(
        project_id=project_id,
        project_name=project_name,
        project_description=project_description,
        folder_pointer=local_project_id
    )
