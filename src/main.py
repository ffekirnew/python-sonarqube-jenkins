from typing import Optional, TypedDict

from fastapi import FastAPI


class Task(TypedDict):
    id: int
    description: str
    completed: bool


class CreateTaskDto(TypedDict):
    task_id: int
    description: str


Api = FastAPI(
    title="Task Management API",
    version="1.0.0",
    description="""
    A simple API for managing tasks. You can create, read, update, and delete tasks.
    """,
)

tasks: dict[int, Task] = {}  # In-memory task storage


@Api.get("/tasks/")
def get_all_tasks():
    if not tasks:
        return {"message": "No tasks found."}
    return tasks


@Api.post("/tasks/")
def create_task(create_task_dto: CreateTaskDto):
    task_id = create_task_dto["task_id"]
    if task_id in tasks:
        return {"error": "Task ID already exists."}

    tasks[task_id] = Task(
        {
            "id": task_id,
            "description": create_task_dto["description"],
            "completed": False,
        }
    )
    return {"message": "Task created successfully."}


@Api.get("/tasks/{task_id}")
def read_task(task_id: int):
    task = tasks.get(task_id)
    if not task:
        return {"error": "Task not found."}
    return task


@Api.put("/tasks/{task_id}")
def update_task(
    task_id: int, description: Optional[str] = None, completed: Optional[bool] = None
):
    task = tasks.get(task_id)
    if not task:
        return {"error": "Task not found."}
    if description is not None:
        task["description"] = description
    if completed is not None:
        task["completed"] = completed
    return {"message": "Task updated successfully."}


@Api.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        return {"error": "Task not found."}
    del tasks[task_id]
    return {"message": "Task deleted successfully."}
