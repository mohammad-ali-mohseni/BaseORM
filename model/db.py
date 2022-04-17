import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = db.create_engine('mysql://root:toor@127.0.0.1:3306/stylight')

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
