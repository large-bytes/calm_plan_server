
def test_post_adds_data_to_test_db(test_db_client):
    response = test_db_client.post("/users/",
                                json ={'username': 'User2', 'email': "email2@email.com", 'password': "87654321",  'disabled': False})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "User2"
    assert data["email"] == "email2@email.com"
    assert data["hashed_password"].startswith('$2b$') == True 
    assert data["disabled"] == False

#TODO
# def test_user_can_delete_self(auth_client):
#     response = auth_client.delete("/users/me")
#     assert response.status_code == 422

def test_update_user_by_id(auth_client):
    response = auth_client.patch("/users/1",
                                json ={"username": "USER2", "password": "newpassword123", "email": "new2@gmail.com"})

    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "USER2"
    assert data["hashed_password"].startswith("$2b$")
    assert data["id"] == 1
    assert data["email"] == "new2@gmail.com"
