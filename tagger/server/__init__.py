import os
import subprocess
import textwrap
import time

from flask import Flask, send_from_directory, Response

from tagger.server.handlers import _add_static_prefix


REL_STATIC_DIR = "tagger/build"
DEFAULT_GUNICORN_HOST = "0.0.0.0"
DEFAULT_GUNICORN_PORT  = 3000

app = Flask(__name__, static_folder=REL_STATIC_DIR)
STATIC_DIR = os.path.join(app.root_path, REL_STATIC_DIR)


@app.route(_add_static_prefix("/"))
def serve():
  if os.path.exists(os.path.join(STATIC_DIR, "index.html")):
    return send_from_directory(STATIC_DIR, "index.html")

  text = textwrap.dedent(
    """
    Unable to display tagger UI - landing page (index.html) not found.
    """
  )
  return Response(text, mimetype="text/plain")


@app.route("/time")
def get_current_time():
  return {"time": "Hello i am Sam"}


def build_gunicorn_command(
  host: str = DEFAULT_GUNICORN_HOST, 
  port: int = DEFAULT_GUNICORN_PORT
):
  cmd = f"gunicorn -b {host}:{port} {app.root_path}.:app"
  return cmd


def _run_server():
  print(STATIC_DIR)
  full_command = build_gunicorn_command()
  process = subprocess.Popen(full_command, text=True)
