from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy') # create engine that will interact with dockerized PostgreSQL DB
Session = sessionmaker(bind=engine) #SQLalchemy ORM session

Base = declarative_base() # base class for our classes definitions