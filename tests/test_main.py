from ..main import app, task_list

def setup_function():
    task_list.clear()

    
def test_read_tasks_from_tasks_list(client):
    response = client.get("/tasks_list")
    assert response.status_code == 200
    assert response.json() == {
    "all_tasks": []
}
    
def test_get_all_tasks_from_db(client, add_tasks_to_db):
    response = client.get("/tasks")
    assert response.status_code == 200


#  write a test to confirm test db is empty

#  write a fixture to seed database 
#  write test to get all 