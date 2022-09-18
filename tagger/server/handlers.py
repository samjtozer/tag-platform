import os


STATIC_PREFIX_ENV_VAR = "_TAGGER_STATIC_PREFIX"


def _add_static_prefix(route):
    prefix = os.environ.get(STATIC_PREFIX_ENV_VAR)
    if prefix:
        return prefix + route
    return route
  