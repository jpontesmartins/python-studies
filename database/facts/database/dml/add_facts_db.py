from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..ddl.config import db_path

engine = create_engine(db_path, echo=True)
Session = sessionmaker(bind=engine, autoflush=False)
session = Session()

def add(fact):
    session.add(fact)
    session.commit()

