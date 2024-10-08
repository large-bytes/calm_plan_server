from logging import Formatter

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from prod_db import database

base = database.Base

#USER MODEL CLASS -
class User(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(10), nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String(8), nullable=False)
    is_active = Column(Boolean, default=True)

    tasks = relationship("Task", back_populates="user")


# TASK MODEL CLASS - 
class Task(base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    priority = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="tasks")

    __table_args__ = {'extend_existing': True}


