from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base
# load environment variables
import dotenv
import os
dotenv.load_dotenv()

# TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")
TEST_DATABASE_URL = 'postgresql://tomfyfe@5432/calm_plan_test/'
engine = create_engine(
    TEST_DATABASE_URL
)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_test_db():
    Base.metadata.create_all(bind=engine)

def drop_test_db():
    Base.metadata.drop_all(bind=engine)