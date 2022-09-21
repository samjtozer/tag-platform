from sqlalchemy import create_engine

from tagger.models.projects import Project
from tagger.definitions import REPO_ROOT_DIR, DEFAULT_DB_NAME


engine = create_engine(f"sqlite:///{REPO_ROOT_DIR}/{DEFAULT_DB_NAME}")


def _add_project_item(project_id: str, project_name: str, project_description: str, folder_pointer: int):
    new_project_item = Project(
        project_id=project_id,
        name=project_name,
        description=project_description,
        folder_pointer=folder_pointer
    )
    print(new_project_item)
