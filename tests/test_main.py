from fastapi.testclient import TestClient
from ..main import app
from ..database import get_db
from  . utils import override_get_db

client = TestClient(app)
app.dependency_overrides[get_db] = override_get_db

def test_returns_all_test_data():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json == [{"id":"1", "name":"Learn JavaScript", "priority":"five"},
                             {"id":"2", "name":"Learn RUST", "priority":"four"}]
