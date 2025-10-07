from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATA_URL = "postgresql://postgres:admin@localhost:5432/escola"

engine = create_engine(DATA_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()