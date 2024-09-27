from pydantic import BaseModel

class TaskBase(BaseModel):
    name: str
    priority: str
    
class TaskCreate(TaskBase):   
    pass

#Task inherits form TaskBase 
class Task(TaskBase):
    id: int

class TaskUpdate(BaseModel):
    name: str | None = None
    priority: str | None = None

    class ConfigDict:
        orm_mode = True

