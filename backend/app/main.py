from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Todo(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    is_completed: bool = False  # 'completed' を 'is_completed' に変更

todos = []
todo_id_counter = 1

@app.post("/todos/", response_model=Todo)
def create_todo(todo: Todo):
    global todo_id_counter
    todo.id = todo_id_counter
    todo_id_counter += 1
    todos.append(todo)
    return todo

@app.get("/todos/", response_model=List[Todo])
def read_todos():
    return todos

@app.get("/todos/{todo_id}", response_model=Todo)
def read_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            updated_todo.id = todo_id
            todos[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}", response_model=Todo)
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            return todos.pop(index)
    raise HTTPException(status_code=404, detail="Todo not found")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API! Go to /docs for the API documentation."}