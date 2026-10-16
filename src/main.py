
from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="Task Manager API",
    description="A simple REST API to manage tasks",
    version="1.0.0"
)


# Request model for creating a task
class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)


# Request model for updating a task
class TaskUpdate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    completed: bool


# Response model for a task
class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool


# Temporary in-memory storage
tasks = {}
next_task_id = 1


# GET: Retrieve all tasks
@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks():
    return list(tasks.values())


# GET: Retrieve one task by ID
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return tasks[task_id]


# POST: Create a task
@app.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED
)
def create_task(task: TaskCreate):
    global next_task_id

    new_task = {
        "id": next_task_id,
        "title": task.title.strip(),
        "completed": False
    }

    if not new_task["title"]:
        raise HTTPException(
            status_code=422,
            detail="Task title cannot be empty"
        )

    tasks[next_task_id] = new_task
    next_task_id += 1

    return new_task


# PUT: Replace a task's editable fields
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    title = task.title.strip()

    if not title:
        raise HTTPException(
            status_code=422,
            detail="Task title cannot be empty"
        )

    updated_task = {
        "id": task_id,
        "title": title,
        "completed": task.completed
    }

    tasks[task_id] = updated_task
    return updated_task


# DELETE: Remove a task
@app.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    del tasks[task_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
