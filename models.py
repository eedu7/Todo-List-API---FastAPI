from sqlalchemy import Column, Integer, String, Boolean
from .database import Base


class TodoItem(Base):
    __tablename__: str = "todo_items"
    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title: str = Column(String(255), index=True)
    description: str = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
