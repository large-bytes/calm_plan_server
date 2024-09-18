from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base
# load environment variables
from dotenv import load_dotenv
import os
load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

print("metadata")
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()