from flask import Blueprint


VERSION = 1.0
BLUEPRINT_NAME = "project"
project = Blueprint(BLUEPRINT_NAME, __name__)


def _wrap_with_version(endpoint: str):
    if endpoint[0] == "/":
        return f"/{VERSION}{endpoint}"
    return f"/{VERSION}/{endpoint}"


@project.endpoint(_wrap_with_version("/create_new_project"), methods=["POST"])
def get_projects():
    return {}
