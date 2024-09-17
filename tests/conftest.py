import pytest

from fastapi.testclient import TestClient
from . test_db import TestSessionLocal, create_test_db, drop_test_db
from ..database import get_db
from ..main import app
from ..models import Task



def override_get_db():
    try:
        test_db = TestSessionLocal()
        yield test_db
    finally:
        test_db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="function")
def test_db_client():
    create_test_db()
    yield TestClient(app)
    drop_test_db()

@pytest.fixture(scope="function")
def populate_test_db():
    test_session = TestSessionLocal()
    tasks = [Task(id=1, name="test name1", priority="five"), Task(id=2, name="test name2", priority="one")]

    test_session.add_all(tasks)
    test_session.commit()

    yield tasks

    test_session.close()
