
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import close_all_sessions
from fastapi.testclient import TestClient
from ..main import app

from sqlalchemy_utils import create_database, drop_database, database_exists
from .. import database
base = database.Base

from . utils import TEST_DB_URL, TestDatabase

client = TestClient(app)


@pytest.fixture(scope="session", autouse=True)
def create_and_delete_test_db():
    print("create and delete db - confest")
    if database_exists(TEST_DB_URL):
        print("db exists - conftest")
        drop_database(TEST_DB_URL)
    create_database(TEST_DB_URL)
    print("db created - conftest")

    test_engine = create_engine(TEST_DB_URL,  pool_pre_ping=True)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
    base.metadata.create_all(bind=test_engine)
    test_db = SessionLocal()
    try:
        print("test_db_session - conftest")
        testdb_util = TestDatabase(test_db)
        testdb_util.populate_test_database()
        # base.metadata.create_all(bind=test_engine)
        yield  test_db
        print('yield test_db_session - conftest')
    finally:
        test_db.close()
        print("session closed- conftest")

    close_all_sessions()
    drop_database(TEST_DB_URL)
    print("Test database cleaned up")

@pytest.fixture(scope="session", autouse=True)
def client():
    return TestClient(app)

# @pytest.fixture(scope="module")
# def add_tasks_to_db(test_db):
#     db = test_db()
#     new_task1 = Task(name="Learn JavaScript", priority="five")
#     new_task2 = Task(name="Learn RUST", priority="four")
#     print("2 new tasks added")
#
#     db.add_all([new_task1, new_task2])
#     print("db add all tasks")
#
#     db.commit()
#
#     for task in [new_task1, new_task2]:
#         db.refresh(task)
#     yield [new_task1, new_task2]
#
#     db.query(Task).delete()
#     db.commit()
#
# @pytest.fixture(scope="module")

#
#
# @pytest.fixture(scope="module")
# def get_test_bd(test_db, add_tasks_to_db):
#     db = test_db()
#     try:
#         yield db
#     finally:
#         db.close()