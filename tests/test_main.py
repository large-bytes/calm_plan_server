from fastapi.testclient import TestClient

from ..main import app, tasks 

client = TestClient(app)

def setup_function():
    tasks.clear()
    
def test_read_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == {
    "all_tasks": []
}

