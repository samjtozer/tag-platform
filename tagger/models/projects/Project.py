from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Project(Base):
    __tablename__ = "project"
    project_id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"<Project id={self.project_id} name={self.name} />"
