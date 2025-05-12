from src.common.exception import ApplicationException
from src.domain.dtos import CreateTaskDto, UpdateTaskDto
from src.infrastructure.task_repository import TaskRepository

# Test creating a new task
def test_create_task():
    # Arrange: create repository and task data
    repo = TaskRepository()
    task_data = CreateTaskDto(description="New Task")

    # Act: create the task
    task = repo.create_task(task_data)

    # Assert: check task properties
    assert task["description"] == "New Task"
    assert not task["completed"]

# Test retrieving all tasks
def test_get_all_tasks():
    # Arrange: create repository
    repo = TaskRepository()

    # Act: get all tasks
    tasks = repo.get_all()

    # Assert: at least one task should exist (sample task)
    assert len(tasks) >= 1

# Test retrieving a specific task by ID
def test_get_task():
    # Arrange: create repository
    repo = TaskRepository()

    # Act: get task with sample ID
    task = repo.get(1000)  # Sample task ID

    # Assert: task should exist and have correct description
    assert task is not None
    assert task["description"] == "Sample task"

# Test retrieving a nonexistent task returns None
def test_get_nonexistent_task():
    # Arrange: create repository
    repo = TaskRepository()

    # Act: try to get a task that doesn't exist
    task = repo.get(9999)

    # Assert: should return None
    assert task is None

# Test deleting a task
def test_delete_task():
    # Arrange: create repository and a new task
    repo = TaskRepository()
    create_task_data = CreateTaskDto(description="Sample task")
    task_data = repo.create_task(create_task_data)

    # Act: delete the created task
    task = repo.delete_task(task_data["id"])

    # Assert: task should be deleted and not retrievable
    assert task["description"] == "Sample task"
    assert repo.get(task_data["id"]) is None

# Test deleting a nonexistent task raises exception
def test_delete_nonexistent_task():
    # Arrange: create repository
    repo = TaskRepository()

    # Act & Assert: deleting nonexistent task should raise ApplicationException
    try:
        repo.delete_task(9999)
    except ApplicationException:
        pass
    else:
        assert False, "Expected ApplicationException"

# Test updating a task
def test_update_task():
    # Arrange: create repository and update data
    repo = TaskRepository()
    update_data = UpdateTaskDto(description="Updated Task", completed=True)

    # Act: update the sample task
    task = repo.update_task(1000, update_data)  # Sample task ID

    # Assert: task should be updated with new data
    assert task["description"] == "Updated Task"
    assert task["completed"]

# Test updating a nonexistent task raises exception
def test_update_nonexistent_task():
    # Arrange: create repository and update data
    repo = TaskRepository()
    update_data = UpdateTaskDto(description="Updated Task", completed=True)

    # Act & Assert: updating nonexistent task should raise ApplicationException
    try:
        repo.update_task(9999, update_data)
    except ApplicationException:
        pass
    else:
        assert False, "Expected ApplicationException"
