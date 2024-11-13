def test_users_returns_client_gives_200(test_db_client):
    response = test_db_client.get("/users")
    assert response.status_code == 200

def test_returns_empty_list_for_response(test_db_client):
    response = test_db_client.get("/users")
    assert response.json() == []

def test_db_is_populated_with_test_data(test_db_client, populate_test_db):
    response = test_db_client.get("/users")
    assert response.json() == [{'username': 'User1', 'id': 1, 'email': "email@email.com", 'password': "12345678",  'is_active': True}]

def test_post_adds_data_to_test_db(test_db_client):
    response = test_db_client.post("/users/",
                                   json ={'username': 'User2', 'id': 1, 'email': "email2@email.com", 'password': "87654321",  'is_active': True})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "User2"
    assert data["email"] == "email2@email.com"
    assert data["id"] == 1
    assert data["password"] == '87654321'
    assert data["is_active"] == True

