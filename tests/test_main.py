def test_returns_client_gives_200(client):
    response = client.get("/tasks")
    assert response.status_code == 200

def test_returns_test_data(client, create_and_delete_test_db):
    response = client.get("/tasks")
    response_data = response.json()
    print(response_data)
    assert response.json == [{"id":"1", "name":"Learn JavaScript", "priority":"five"},
                             {"id":"2", "name":"Learn RUST", "priority":"four"}]
