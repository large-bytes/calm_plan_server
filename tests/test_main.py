from ..main import app, tasks

def setup_function():
    tasks.clear()
    
def test_read_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == {
    "all_tasks": []
}

# add test_db fixture - this should create a test db 
