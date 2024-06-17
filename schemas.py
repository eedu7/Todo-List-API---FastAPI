from pydantic import BaseModel


class TodoItemBase(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False


class TodoItemCreate(TodoItemBase):
    pass


class TodoItem(TodoItemBase):
    id: int

    class Config:
        from_attributes = True  # orm_mode has been renamed to form_attributes
