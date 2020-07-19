import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from .config import db_path

engine = create_engine(db_path, echo=False)
Base = declarative_base()

class Fact(Base):
    __tablename__ = 'facts'

    id = Column(Integer, primary_key=True)
    what = Column(String)
    when = Column(String)
    where = Column(String)

    def __repr__(self):
        return "<Fact(what='%s', when='%s', where='%s')>" % (self.what, self.when, self.where)

Base.metadata.create_all(engine)
