from typing import Optional, Union
from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: Union[str, None] = None
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class Todo(TodoBase):
    id: int

    class Config:
        from_attributes = True  # 以前の orm_mode = True の代わり