from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from . import schemas, crud
from .database import engine, Base, get_db

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/todo/", response_model=schemas.TodoItem)
async def create_todo_item(todo: schemas.TodoItemCreate, db: Session = Depends(get_db)):
    return crud.create_todo_item(db=db, todo=todo)


@app.get("/todo/", response_model=list[schemas.TodoItem])
async def read_todo_items(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
):
    return crud.get_todo_items(db, skip=skip, limit=limit)


@app.get("/todo/{todo_id}", response_model=schemas.TodoItem)
async def read_todo_item(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo_item(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo Item not found"
        )
    return db_todo


@app.delete("/todo/{todo_id}", response_model=schemas.TodoItem)
def delete_todo_item(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.delete_todo_items(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return db_todo


@app.put("/todo/{todo_id}", response_model=schemas.TodoItem)
async def update_todo_item(
    todo_id: int, todo: schemas.TodoItemCreate, db: Session = Depends(get_db)
):
    db_todo = crud.update_todo_item(db, todo_id=todo_id, todo=todo)
    if db_todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo Item not found"
        )
    return db_todo
