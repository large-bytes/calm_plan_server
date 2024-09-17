from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..database import Base

TEST_DATABASE_URL = "postgresql://tomfyfe@localhost:5432/calm_plan_test"

engine = create_engine(
    TEST_DATABASE_URL
)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_test_db():
    Base.metadata.create_all(bind=engine)

def drop_test_db():
    Base.metadata.drop_all(bind=engine)