import pytest

from fastapi.testclient import TestClient
from . test_db import TestSessionLocal, create_test_db, drop_test_db
from ..database import get_db
from ..main import app

def override_get_db():
    try:
        test_db = TestSessionLocal()
        yield test_db
    finally:
        test_db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module")
def test_db_client():
    create_test_db()

    yield TestClient(app)

    drop_test_db()
