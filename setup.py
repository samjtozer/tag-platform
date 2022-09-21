import os
from setuptools import setup, find_packages


CORE_REQUIREMENTS = [
  "click>=7.0",
  "Flask",
  "gunicorn"
]


# Get a list of all files in the JS directory to include in our module
def package_files(directory):
    paths = []
    for (path, _, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join("..", path, filename))
    return paths


js_files = package_files("tagger/server/client/build")


setup(
  name="tagger",
  author="Sam Tozer",
  install_requires=CORE_REQUIREMENTS,
  packages=find_packages(exclude=[]),
  package_data={"tagger": js_files},
  entry_points="""
    [console_scripts]
    tagger=tagger.cli:cli
  """
)
