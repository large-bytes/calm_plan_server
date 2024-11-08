def test_users_return_client_gives_200(test_db_client, populate_test_db):
    response = test_db_client.get("/users")
    assert response.status_code == 200

