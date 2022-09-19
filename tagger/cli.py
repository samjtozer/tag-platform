import os

import click
from tagger.server import _run_server

from tagger.definitions import REPO_ROOT_DIR, TAGGER_ROOT_DIR, DEFAULT_DB_NAME
from tagger.models import _load_database, _create_database
from tagger.models.handler import DatabaseHandler
from tagger.server import app
from tagger.utils import (
    file_exists,
    folder_exists,
    create_init_config,
    create_directory
)
from tagger.project import create_project as _create_project


@click.group()
def cli():
    pass


@cli.command()
def init():
    """Initialise a tagger project"""
    if folder_exists(f"{REPO_ROOT_DIR}/{TAGGER_ROOT_DIR}"):
        click.secho("tagger has already been instantiated", fg="red")
    else:
        click.secho("Instantiating tagger...🚀", fg="green")
        os.mkdir(f"{REPO_ROOT_DIR}/{TAGGER_ROOT_DIR}")
        create_init_config(f"{REPO_ROOT_DIR}/{TAGGER_ROOT_DIR}")
        create_directory(f"{REPO_ROOT_DIR}/{TAGGER_ROOT_DIR}/projects")
        click.secho("Successfully instantiated ✅ - run `tagger --help` for available commands")


@cli.command()
@click.option("--project-name", required=True, type=str, help="Name of your new tagging project.")
@click.option("--project-description", required=False, type=str, help="Description of the project.")
def create_project(project_name: str, project_description: str = ""):
    """Create a new tagging project"""
    click.secho(f"Creating project: {project_name}", fg="green")
    _create_project(project_name, project_description)


@cli.command()
def ui():
    """Run the tagger web app locally"""
    click.echo("Running local server")
    server_command = _run_server()
    click.echo(server_command)


@cli.command()
@click.option("--database-path", required=False, type=str, help="Path to existing database file.")
def server(database_path: str):
    """Run the tagger server"""
    engine = None
    """Run the tagger web server locally"""
    if not database_path:
        # Then create a local sqlite database
        click.echo("No database path supplied. Creating a new db instance...")
        # Perform a sanity check to make sure the default db isn't on disk
        click.echo(REPO_ROOT_DIR)
        if file_exists(f"{REPO_ROOT_DIR}/{DEFAULT_DB_NAME}"):
            click.secho(
                f"Detected a database file in the project named {DEFAULT_DB_NAME}. Please move this file before trying to run the tagger server.",
                fg="red"
            )
            engine = _load_database(f"{REPO_ROOT_DIR}/{DEFAULT_DB_NAME}")
            click.secho("Loaded database...", fg="green")

        else:
            url = f"sqlite:///{REPO_ROOT_DIR}/tagr.db"
            engine = _create_database(url=url)
            click.secho("Successfully created database file.", fg="green")
    else:
        # Check if the file exists
        if file_exists(database_path):
            engine = _load_database(database_path)
            click.secho("Successfully loaded database file.", fg="green")

    if not engine:
        raise Exception

    # We need to check all tables are loaded in the database
    DatabaseHandler.ensure_db_init_state(engine)
    click.secho("Database schemas initialised", fg="green")

    # Now the database is loaded, we can run the server
    app.run(debug=True)


if __name__ == "__main__":
    cli()
