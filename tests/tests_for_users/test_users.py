import pytest

def test_users_returns_client_gives_200(test_db_client):
    response = test_db_client.get("/users")
    assert response.status_code == 200

def test_returns_empty_list_for_response(test_db_client):
    response = test_db_client.get("/users")
    assert response.json() == []

def test_db_is_populated_with_test_data(test_db_client, populate_test_db):
    response = test_db_client.get("/users")
    assert response.json() == [{'username': 'User1', 'id': 1, 'email': "email@email.com", 'hashed_password': "12345678",  'disabled': False}]

def test_post_adds_data_to_test_db(test_db_client):
    response = test_db_client.post("/users/",
                                json ={'username': 'User2', 'email': "email2@email.com", 'hashed_password': "87654321",  'disabled': False})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "User2"
    assert data["email"] == "email2@email.com"
    assert data["hashed_password"] == '87654321'
    assert data["disabled"] == False

def test_get_user_by_id(test_db_client, populate_test_db):
    # Requests with a valid id
    response = test_db_client.get("/users/1")
    assert response.status_code == 200

    # Requests with an invalid id
    response1 = test_db_client.get("/users/a")
    assert response1.status_code == 422

    # # Request with None as ID
    response2 = test_db_client.get("/users/None")
    assert response2.status_code == 422
    #
    # Request with non-existing yet valid task ID
    response3 = test_db_client.get("/users/9999")
    assert response3.status_code == 404
    #
    data = response.json()
    assert data["username"] == "User1"
    assert data["email"] == "email@email.com"
    assert data["id"] == 1
    assert data["hashed_password"] == "12345678"
    assert data["disabled"] == False

def test_delete_task(test_db_client, populate_test_db):
    response = test_db_client.get("/users")
    assert response.status_code == 200
    assert len(response.json()) == 1

    delete_response = test_db_client.delete("/users/1")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"ok": True}

    response2 = test_db_client.get("/users")
    assert response2.status_code == 200
    data = response2.json()
    print(data)

    assert len(data) == 0

def test_update_user_by_id(test_db_client, populate_test_db):
    response = test_db_client.patch("/users/1",
                                json ={"username": "USER2", "hashed_password": "12345678", "email": "new2@gmail.com"})

    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "USER2"
    assert data["hashed_password"] == "12345678"
    assert data["id"] == 1
    assert data["email"] == "new2@gmail.com"
