from pydantic import BaseModel

class TaskBase(BaseModel):
    name: str
    priority: str
    
class TaskCreate    
    pass

#Task inherits form TaskBase 
class Task(TaskBase):
    id: int
    

    class Config:
    orm_mode = True

