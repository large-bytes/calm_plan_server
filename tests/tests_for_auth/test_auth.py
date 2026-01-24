def test_auth_me_returns_current_user(auth_client):
    response = auth_client.get("auth/me")

    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "User1"
    assert data["email"] == "email@email.com"

def test_auth_me_returns_401_without_token(test_db_client):
    response = test_db_client.get("/auth/me")
    assert response.status_code == 401