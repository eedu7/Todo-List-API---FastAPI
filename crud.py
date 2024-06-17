from sqlalchemy.orm import Session

from . import models, schemas


def get_todo_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.TodoItem).offset(skip).limit(limit).all()


def get_todo_item(db: Session, todo_id: int):
    return db.query(models.TodoItem).filter(models.TodoItem.id == todo_id).first()


def create_todo_item(db: Session, todo: schemas.TodoItemCreate):
    db_todo = models.TodoItem(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo_items(db: Session, todo_id: int):
    db_todo = db.query(models.TodoItem).filter(models.TodoItem.id == todo_id).first()
    db.delete(db_todo)
    db.commit()
    return db_todo


def update_todo_item(db: Session, todo_id: int, todo: schemas.TodoItemCreate):
    db_todo = db.query(models.TodoItem).filter(models.TodoItem.id == todo_id).first()
    if db_todo:
        for key, value in todo.dict().items():
            setattr(db_todo, key, value)
        db.commit()
        db.refresh(db_todo)
    return db_todo
