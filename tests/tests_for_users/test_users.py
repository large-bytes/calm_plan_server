def test_users_returns_client_gives_200(test_db_client):
    response = test_db_client.get("/users")
    assert response.status_code == 200

def test_returns_empty_list_for_response(test_db_client):
    response = test_db_client.get("/users")
    assert response.json() == []

def test_db_is_populated_with_test_data(test_db_client, populate_test_db):
    response = test_db_client.get("/users")
    assert response.json() == [{'username': 'User1', 'id': 1, 'email': "email@email.com", 'password': "12345678",  'is_active': True}]