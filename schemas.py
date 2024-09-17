from pydantic import BaseModel

class TaskBase(BaseModel):
    name: str
    priority: str
    
class TaskCreate(TaskBase):   
    name: str
    priority: str

#Task inherits form TaskBase 
class Task(TaskBase):
    id: int
    

    class ConfigDict:
        orm_mode = True

