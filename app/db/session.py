from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# create a SQLAlchemy engine
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)

# each instance of the SessionLocal class will be a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
