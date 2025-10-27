from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,URL
from sqlalchemy.ext.declarative import declarative_base
from app.core.config import config



url_object = URL.create(
    drivername='postgresql+psycopg2',
    host=config.DB_HOST,
    port=config.DB_PORT,
    username=config.DB_USER,
    password=config.DB_PASSWORD,
    database=config.DB_NAME
)

engine = create_engine(url=url_object)

BASE = declarative_base()

localSession = sessionmaker(bind=engine)  
