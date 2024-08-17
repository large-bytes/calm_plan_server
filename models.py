from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

# TASK MODEL CLASS - 
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    priority = Column(String, index=True)

