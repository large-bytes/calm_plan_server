from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..database import Base
from ..models import Task

TEST_DATABASE_URL = "postgresql://tomfyfe@localhost:5432/calm_plan_test"

engine = create_engine(
    TEST_DATABASE_URL
)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_test_db():
    Base.metadata.create_all(bind=engine)
    # task1 = Task("task1", "5")
    # print("task1")
    # with TestSessionLocal() as test_session:
    #     test_session.add(task1)
    #     test_session.commit()


def drop_test_db():
    Base.metadata.drop_all(bind=engine)