from abc import abstractmethod

from src.domain.dtos import CreateTaskDto, UpdateTaskDto
from src.domain.task import Task

# Abstract base class for Task repository.
class ABCTaskRepository:
    @abstractmethod
    def create_task(self, task_data: CreateTaskDto) -> Task:
        """
        Create a new task using the provided data.
        """
        ...

    @abstractmethod
    def get_all(self) -> list[Task]:
        """
        Retrieve all tasks.
        """
        ...

    @abstractmethod
    def get(self, task_id: int) -> Task | None:
        """
        Retrieve a single task by its ID.
        Returns None if not found.
        """
        ...

    @abstractmethod
    def delete_task(self, task_id: int) -> Task:
        """
        Delete a task by its ID.
        Returns the deleted task.
        """
        ...

    @abstractmethod
    def update_task(self, task_id: int, task_data: UpdateTaskDto) -> Task:
        """
        Update an existing task with new data.
        Returns the updated task.
        """
        ...
