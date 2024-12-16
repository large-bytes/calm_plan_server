

def test_tasks_returns_client_gives_200(test_db_client, populate_test_db):
    response = test_db_client.get("/users/1")
    assert response.status_code == 200