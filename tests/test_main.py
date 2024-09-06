from fastapi.testclient import TestClient
from fastapi import FastAPI, HTTPException, Depends
from ..import models

from ..main import app
from ..database import get_db
from  . utils import override_get_db
from sqlalchemy.orm import Session

client = TestClient(app)
app.dependency_overrides[get_db] = override_get_db

def test_returns_all_test_data(db: Session = Depends(get_db)):
    response = client.get("/tasks")
    assert response.status_code == 200
    response_data = response.json()
    print(response_data)
    assert len(response_data) == 2
    assert any(task['name'] == "Learn JavaScript" and task['priority'] == "five" for task in response_data)
    # assert response.json == [{"id":"1", "name":"Learn JavaScript", "priority":"five"},
    #                          {"id":"2", "name":"Learn RUST", "priority":"four"}]
