from typing import Optional

from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    name: str
    priority: str
    
class TaskCreate(TaskBase):   
    pass

#Task inherits form TaskBase 
class Task(TaskBase):
    id: int

class TaskUpdate(BaseModel):
    name: Optional[str] = Field(default=None)
    priority: Optional[str] = Field(default=None)

    class ConfigDict:
        orm_mode = True

