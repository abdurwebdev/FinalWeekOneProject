from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
import os

URL = os.getenv("DATABASE_URL")

engine = create_engine(URL)

SessionLocal = sessionmaker(
  autocommit = False,
  autoflush = False,
  bind = engine
)

def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()

Base = declarative_base()