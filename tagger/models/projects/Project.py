from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Project(Base):
    __tablename__ = "project"
    uid = Column(Integer, primary_key=True)
    project_id = Column(String)
    name = Column(String)
    description = Column(String)
    folder_pointer = Column(Integer)

    def __repr__(self):
        return f"<Project id={self.project_id} name={self.name} />"
