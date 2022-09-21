from sqlalchemy import create_engine


def _load_database(url):
    return create_engine(f"sqlite:///{url}")


def _create_database(url):
    return create_engine(url)
