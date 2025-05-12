from fastapi.testclient import TestClient
from src.main import Api

# Create a TestClient using the FastAPI app instance
client = TestClient(Api)

def test_create_task():
    # Test creating a new task
    response = client.post(
        "/tasks/",
        json={"description": "Test Task"},
    )
    assert response.status_code == 200
    assert "Task created successfully." in response.json().get("message")

def test_read_task():
    # Create a task first to ensure it exists
    client.post("/tasks/", json={"description": "New Task"})
    # Test reading the created task
    response = client.get("/tasks/1001")
    assert response.status_code == 200
    assert response.json().get("data")["description"] == "New Task"

def test_update_task():
    # Create a task first to update it
    client.post("/tasks/", json={"description": "Test Task"})
    # Test updating the created task
    response = client.put(
        "/tasks/1001", json={"description": "Updated Task", "completed": True}
    )
    assert response.status_code == 200
    assert "Task updated successfully." in response.json().get("message")

def test_delete_task():
    # Create a task first to delete it
    client.post("/tasks/", json={"description": "Test Task"})
    # Test deleting the created task
    response = client.delete("/tasks/1001")
    assert response.status_code == 200
    assert "Task deleted successfully." in response.json().get("message")

def test_task_not_found():
    # Test retrieving a non-existent task
    response = client.get("/tasks/999")
    assert response.status_code == 404
    assert "Task not found." in response.json().get("errors")
