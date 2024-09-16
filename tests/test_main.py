import pytest

def test_returns_client_gives_200(test_db_client):
    response = test_db_client.get("/tasks")
    assert response.status_code == 200

def test_returns_empty_list_for_response(test_db_client):
    response = test_db_client.get("/tasks")
    assert response.json() == []

