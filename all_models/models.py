from sqlalchemy import Column, Integer, String

from prod_db import database

base = database.Base

# TASK MODEL CLASS - 
class Task(base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    priority = Column(String, index=True)

    __table_args__ = {'extend_existing': True}


