# Day 5 — FastAPI Task Manager API

## Project Overview

This project converts the Day 2 Task Manager into a REST API using FastAPI and Python.

The API allows users to create, view, update, and delete tasks. Tasks are stored in memory while the server is running.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic
- Swagger UI

## Features

- Create a task
- View all tasks
- View a task by ID
- Update a task
- Delete a task
- Validate request data
- Return appropriate HTTP status codes
- Handle tasks that do not exist

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{task_id}` | Get one task |
| POST | `/tasks` | Create a task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

## Installation and Setup

1. Create and activate a Python virtual environment.
2. Install the dependencies:

   `python -m pip install -r requirements.txt`

3. Start the API from the project root folder:

   `python -m uvicorn src.main:app --reload`

4. Open the API documentation:

   `http://127.0.0.1:8000/docs`

## Example Request

To create a task, send a POST request to `/tasks` with this JSON body:

```json
{
  "title": "Learn FastAPI"
}
```

A successful request returns HTTP 201 Created.

## HTTP Status Codes

- `200 OK` — Request completed successfully.
- `201 Created` — Task created successfully.
- `204 No Content` — Task deleted successfully.
- `404 Not Found` — Task ID does not exist.
- `422 Unprocessable Entity` — Request data failed validation.

## Testing

The endpoints were tested using the interactive Swagger UI documentation page provided by FastAPI.

Tests included creating tasks, retrieving tasks, updating a task, deleting a task, and checking an invalid task ID.

## Limitations

Tasks are stored in memory and are not saved permanently. They are lost when the server restarts.

## Learning Outcome

This project demonstrates REST API fundamentals, CRUD operations, request validation, HTTP status codes, and API testing with FastAPI.
