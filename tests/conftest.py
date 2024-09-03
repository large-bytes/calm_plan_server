import pytest
from fastapi.testclient import TestClient
from ..main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..database import Base
# from models import Task


@pytest.fixture(scope="module")
def test_db():
    engine = create_engine(
    "postgresql://tomfyfe@localhost:5432/calm_plan_test")
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    yield TestingSessionLocal
    Base.metadata.drop_all(bind=engine)
    
@pytest.fixture(scope="module")
def add_tasks_to_db(test_db):
    db = test_db()
    new_task1 = Task(name="Learn JavaScript", priority="five")
    new_task2 = Task(name="Learn RUST", priority="four")
    db.add_all([new_task1, new_task2])
    db.commit()
    for task in [new_task1, new_task2]:
        db.refresh(task)
    yield [new_task1, new_task2]
    db.query(Task).delete()
    db.commit()
    db.close()

@pytest.fixture(scope="module")
def client(test_db):
    return TestClient(app)


@pytest.fixture(scope="module")
def get_test_bd(test_db):
    db = test_db()
    try:
        yield db
    finally:
        db.close()