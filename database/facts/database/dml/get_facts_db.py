from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..ddl.create_facts_db import Fact
from ..ddl.config import db_path

engine = create_engine(db_path, echo=False)
Session = sessionmaker(bind=engine, autoflush=False)
session = Session()

def get_all():
    return session.query(Fact).all()

def get_when(param):
    return session.query(Fact).filter(Fact.when == param).all()

