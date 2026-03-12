from model.impl.task import Task
import os
from fastapi import FastAPI
from user_books import user_books
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

user_books()
task_db = Task("tasks.csv", ["title", "description", "completed"])
if not os.path.exists("tasks.csv"):
    task_db.initialize_db()


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = ""
    completed: bool = False


class TaskUpdate(BaseModel):
    title: str
    description: Optional[str] = ""
    completed: bool = False


@app.get("/tasks")
def read_all_tasks():
    return {"tasks": task_db.list_all()}


@app.get("/tasks/{task_id}")
def get_task_by_id(task_id):
    return {"tasks": task_db.get("id", task_id)}


@app.post("/tasks")
def add_new_task(task: TaskCreate):
    task_db.add(task.title, task.description, task.completed)
    return {"message": "Task created"}


@app.put("/tasks/{task_id}")
def update_task(task_id, new_task: TaskUpdate):
    task_db.update(
        task_id,
        {
            "title": new_task.title,
            "description": new_task.description,
            "completed": new_task.completed,
        },
    )
    return {"message": "Task updated"}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    task_db.delete("id", task_id)
    return {"message": "Task deleted"}
