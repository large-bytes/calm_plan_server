import pytest
from ..models import Task




def test_returns_client_gives_200(test_db_client, populate_test_db):
    response = test_db_client.get("/tasks")
    assert response.status_code == 200

def test_returns_empty_list_for_response(test_db_client):
    response = test_db_client.get("/tasks")
    assert response.json() == []


def test_db_is_populated_with_test_data(test_db_client, populate_test_db):
    response = test_db_client.get("/tasks")
    assert response.json() == [{'priority': 'five', 'id': 1, 'name': 'test name1'},
                               {'priority': 'one', 'id': 2, 'name': 'test name2'}]



def test_post_adds_data_to_test_db(test_db_client):
    response = test_db_client.post("/tasks/",
                                   json ={"name": "test_task", "priority": "five"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "test_task"
    assert data["priority"] == "five"
