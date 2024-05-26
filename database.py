from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import configuration

if configuration.ENV == 'test':
    database_url = configuration.DATABASE_URL_TEST
else:
    database_url = configuration.DATABASE_URL_PROD

engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()