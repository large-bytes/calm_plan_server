
import pytest
from fastapi.testclient import TestClient
from ..main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..database import Base
from models import Task


@pytest.fixture(scope="module")
def test_db():

    engine = create_engine("postgresql://tomfyfe@localhost:5432/calm_plan_test")
    testing_session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Create all tables
    Base.metadata.create_all(bind=engine)
    print("tables created")

    yield testing_session_local

    # Drop all tables
    print("Dropping tables...")
    Base.metadata.drop_all(bind=engine)
    print("Test database teardown complete.")
    
@pytest.fixture(scope="module")
def add_tasks_to_db(test_db):
    db = test_db()
    new_task1 = Task(name="Learn JavaScript", priority="five")
    new_task2 = Task(name="Learn RUST", priority="four")
    print("2 new tasks added")

    db.add_all([new_task1, new_task2])
    print("db add all tasks")

    db.commit()

    for task in [new_task1, new_task2]:
        db.refresh(task)
    yield [new_task1, new_task2]

    db.query(Task).delete()
    db.commit()

@pytest.fixture(scope="module")
def client(test_db, add_tasks_to_db):
    return TestClient(app)


@pytest.fixture(scope="module")
def get_test_bd(test_db, add_tasks_to_db):
    db = test_db()
    try:
        yield db
    finally:
        db.close()