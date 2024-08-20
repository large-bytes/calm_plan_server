import pytest
from fastapi.testclient import TestClient
from ..main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..database import Base


SQLALCHEMY_TEST_DATABASE_URL = "postgresql://tomfyfe@localhost:5432/calm_plan_test"

engine = create_engine(
    SQLALCHEMY_TEST_DATABASE_URL
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def get_test_bd():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()