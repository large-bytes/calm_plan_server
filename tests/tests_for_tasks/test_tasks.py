
def test_returns_client_gives_200(test_db_client, populate_test_db):
    response = test_db_client.get("/tasks")
    assert response.status_code == 200

def test_returns_empty_list_for_response(test_db_client):
    response = test_db_client.get("/tasks")
    assert response.json() == []


def test_db_is_populated_with_test_data(test_db_client, populate_test_db):
    response = test_db_client.get("/tasks")
    print(response.json())
    assert response.json() == [{'user_id': None, 'name': 'test name1', 'id': 1, 'priority': 'five', 'user_id':1},
                               {'user_id': None, 'name': 'test name2', 'id': 2, 'priority': 'one', 'user_id':1}]



def test_post_adds_data_to_test_db(test_db_client):
    response = test_db_client.post("/tasks/",
                                   json ={"name": "test_task", "priority": "five"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "test_task"
    assert data["priority"] == "five"
    assert data["id"] == 1


def test_get_task_by_id(test_db_client, populate_test_db):
    # Requests with a valid id
    response = test_db_client.get("/tasks/2")
    assert response.status_code == 200

    # Requests with an invalid id
    response1 = test_db_client.get("/tasks/a")
    assert response1.status_code == 422

    # Request with None as ID
    response2 = test_db_client.get("/tasks/None")
    assert response2.status_code == 422

    # Request with non-existing yet valid task ID
    response3 = test_db_client.get("/tasks/9999")
    assert response3.status_code == 404

    data = response.json()
    # print(data)
    assert data["name"] == "test name2"
    assert data["priority"] == "one"
    assert data["id"] == 2

def test_delete_task(test_db_client, populate_test_db):
    response = test_db_client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json()) == 2

    delete_response = test_db_client.delete("/tasks/2")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"ok": True}

    response2 = test_db_client.get("/tasks")
    assert response2.status_code == 200
    data = response2.json()
    print(data)

    assert len(data) == 1
    assert "test name2" and "one" and 2 not in data

def test_update_task_by_id(test_db_client, populate_test_db):
    response = test_db_client.patch("/tasks/1",
                                   json ={"name": "different task", "priority": "three"})

    assert response.status_code == 200
    data = response.json()

    assert data["name"] == "different task"
    assert data["priority"] == "three"
    assert data["id"] == 1
