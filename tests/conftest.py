import pytest
from fastapi.testclient import TestClient
from ..main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..database import Base

@pytest.fixture(scope="module")
def test_db():
    engine = create_engine(
    "postgresql://tomfyfe@localhost:5432/calm_plan_test")
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    yield TestingSessionLocal
    Base.metadata.drop_all(bind=engine)

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