from sqlalchemy import inspect

from tagger.models.projects import db_tables


class DatabaseHandler:

    @staticmethod
    def ensure_db_init_state(engine):
        # Make sure that the database includes all tables
        for table in db_tables:
            if not inspect(engine).has_table(table.__tablename__):
                # If the table does not exist, create it
                table.__table__.create(bind=engine)
        # TODO Extensive sanity checking of schemas & relationships
