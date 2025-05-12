from src.common.exception import ApplicationException, Exceptions
from src.common.singleton import SingletonMeta
from src.domain.contracts import ABCTaskRepository
from src.domain.dtos import CreateTaskDto, UpdateTaskDto
from src.domain.task import Task

# TaskRepository implements the ABCTaskRepository interface and uses SingletonMeta to ensure a single instance.
class TaskRepository(ABCTaskRepository, metaclass=SingletonMeta):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize the current task ID and a dictionary to store tasks.
        self._curr_id: int = 1001
        self.tasks: dict[int, Task] = {
            1000: Task(id=1000, description="Sample task", completed=False),
        }

    # Create a new task and add it to the repository.
    def create_task(self, task_data: CreateTaskDto) -> Task:
        new_task: Task = {
            "id": self._curr_id,
            "completed": False,
            **task_data,
        }
        self.tasks[self._curr_id] = new_task
        self._curr_id += 1

        return new_task

    # Retrieve all tasks as a list.
    def get_all(self) -> list[Task]:
        return list(self.tasks.values())

    # Retrieve a single task by its ID.
    def get(self, task_id: int) -> Task | None:
        return self.tasks.get(task_id)

    # Delete a task by its ID. Raises an exception if the task does not exist.
    def delete_task(self, task_id: int) -> Task:
        if task_id not in self.tasks:
            raise ApplicationException(
                Exceptions.NotFoundException,
                "Cannot delete task.",
                ["Task ID not found."],
            )

        task = self.tasks[task_id]
        del self.tasks[task_id]

        return task

    # Update an existing task with new data. Raises an exception if the task does not exist.
    def update_task(
        self,
        task_id: int,
        task_data: UpdateTaskDto,
    ) -> Task:
        task = self.get(task_id)
        if task is None:
            raise ApplicationException(
                Exceptions.NotFoundException,
                "Cannot update task.",
                ["Task ID not found."],
            )

        updated_task: Task = {
            "id": task["id"],
            "description": (task_data.get("description", task["description"])),
            "completed": (task_data.get("completed", task["completed"])),
        }
        self.tasks[task_id] = updated_task

        return updated_task
