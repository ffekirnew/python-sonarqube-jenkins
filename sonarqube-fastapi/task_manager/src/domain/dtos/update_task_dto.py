from typing import NotRequired, TypedDict

# Data Transfer Object for updating a task
class UpdateTaskDto(TypedDict):
    # Optional description of the task
    description: NotRequired[str]
    # Optional completion status of the task
    completed: NotRequired[bool]
