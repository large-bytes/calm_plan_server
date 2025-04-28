from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
# load environment variables
from dotenv import load_dotenv
import os
load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "production")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


print("metadata")
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()