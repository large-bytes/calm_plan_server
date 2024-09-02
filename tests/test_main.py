from ..main import app, tasks

def setup_function():
    tasks.clear()
    
def test_read_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == {
    "all_tasks": []
}

#  write a test to confirm test db is empty

#  write a fixture to seed database 
#  write test to get all 