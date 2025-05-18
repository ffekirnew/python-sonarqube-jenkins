from src.common.exception import ApplicationException, Exceptions
from src.domain.dtos.create_task_dto import CreateTaskDto
from src.domain.task import Task


class TaskRepository:
    def __init__(self):
        self.tasks = {}

    def create_task(self, task_data: CreateTaskDto) -> Task:
        task_id = task_data["id"]
        if task_id in self.tasks:
            raise ApplicationException(
                Exceptions.BadRequestException,
                "Cannot create task.",
                ["Task ID already exists."],
            )

        self.tasks[task_id] = task_data
        return self.tasks[task_id]

    def get_all(self) -> list[Task]:
        if not self.tasks:
            raise ApplicationException(
                Exceptions.NotFoundException,
                "Cannot fetch tasks.",
                ["No tasks found."],
            )

        return list(self.tasks.values())

    def get(self, task_id: int) -> Task | None:
        return self.tasks.get(task_id)

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

    def update_task(
        self,
        task_data: CreateTaskDto,
    ) -> Task:
        task_id = task_data["id"]
        if task_id not in self.tasks:
            raise ApplicationException(
                Exceptions.NotFoundException,
                "Cannot update task.",
                ["Task ID not found."],
            )

        self.tasks[task_id] = task_data
        return self.tasks[task_id]
