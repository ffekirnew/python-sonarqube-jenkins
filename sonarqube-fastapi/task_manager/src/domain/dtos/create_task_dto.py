from typing import TypedDict

# Data Transfer Object (DTO) for creating a new task
class CreateTaskDto(TypedDict):
    # Description of the task to be created
    description: str
