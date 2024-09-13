import pytest
import psycopg2

from ..main import app
from fastapi.testclient import TestClient
import pytest_postgresql
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

client = TestClient(app)

# TODO create fixture using 'postgresql' from pytest-postgresql plugin that will create a tasks table'


def test_returns_client_gives_200():
    response = client.get("/tasks")
    assert response.status_code == 200

def test_returns_test_data():
    response = client.get("/tasks")
    response_data = response.json()
    print(response_data)
    assert response.json == []

