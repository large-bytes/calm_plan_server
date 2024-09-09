def test_returns_all_test_data(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    response_data = response.json()
    print(response_data)
    assert len(response_data) == 2
    assert any(task['name'] == "Learn JavaScript" and task['priority'] == "five" for task in response_data)


    # assert response.json == [{"id":"1", "name":"Learn JavaScript", "priority":"five"},
    #                          {"id":"2", "name":"Learn RUST", "priority":"four"}]
