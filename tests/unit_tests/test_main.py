import unittest

from fastapi.testclient import TestClient

from src.main import Api


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(Api)

    def test_create_task(self):
        response = self.client.post(
            "/tasks/",
            json={"task_id": 1, "description": "Test Task"},
        )
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertIn("Task created successfully.",
                      response.json().get("message"))

    def test_read_task(self):
        # Create a task first
        self.client.post(
            "/tasks/", json={"task_id": 1, "description": "Test Task"})
        response = self.client.get("/tasks/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("description"), "Test Task")

    def test_update_task(self):
        # Create a task first
        self.client.post(
            "/tasks/", json={"task_id": 1, "description": "Test Task"})
        response = self.client.put(
            "/tasks/1", json={"description": "Updated Task", "completed": True}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("Task updated successfully.",
                      response.json().get("message"))

    def test_delete_task(self):
        # Create a task first
        self.client.post(
            "/tasks/", json={"task_id": 1, "description": "Test Task"})
        response = self.client.delete("/tasks/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Task deleted successfully.",
                      response.json().get("message"))

    def test_task_not_found(self):
        response = self.client.get("/tasks/999")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Task not found.", response.json().get("error"))


if __name__ == "__main__":
    unittest.main()
