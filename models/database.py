import os
from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base

dbuser = os.environ.get('dbuser') 
dbpass = os.environ.get('dbpass') 
db_adress = os.environ.get('db_adress') 
db_name = os.environ.get('db_name')
# https://docs.sqlalchemy.org/en/20/core/engines.html#mysql
MYSQL_DATABASE_URL = "mysql+mysqldb://{dbuser}:{dbpass}@{db_adress}/{db_name}".format(dbuser=dbuser,dbpass=dbpass,db_adress=db_adress, db_name=db_name)

engine = create_engine(
    MYSQL_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
