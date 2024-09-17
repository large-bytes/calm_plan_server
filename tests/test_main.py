import pytest
from ..models import Task
def test_returns_client_gives_200(test_db_client):
    response = test_db_client.get("/tasks")
    assert response.status_code == 200

def test_returns_empty_list_for_response(test_db_client):
    response = test_db_client.get("/tasks")
    print(response.json())
    assert response.json() == []

def test_post_adds_data_to_test_db(test_db_client):
    response = test_db_client.post("/add_task/",
                                   json ={"name": "test_task", "priority": "five"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "test_task"
    assert data["priority"] == "five"
