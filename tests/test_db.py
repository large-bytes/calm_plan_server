from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from prod_db.database import Base
# load environment variables
from dotenv import load_dotenv
import os
load_dotenv()

TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")

engine = create_engine(
    TEST_DATABASE_URL
)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_test_db():
    Base.metadata.create_all(bind=engine)

def drop_test_db():
    Base.metadata.drop_all(bind=engine)