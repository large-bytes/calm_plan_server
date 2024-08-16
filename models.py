from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

# {"id": "1", "name": "Learn JavaScript", "priority": "five"},

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    priority = Column(String)