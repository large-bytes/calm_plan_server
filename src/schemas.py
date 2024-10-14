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
    user_id: int

class TaskUpdate(BaseModel):
    name: Optional[str] = Field(default=None)
    priority: Optional[str] = Field(default=None)

    class ConfigDict:
        orm_mode = True

#
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    tasks: list[Task] = []

    class ConfigDict:
        orm_mode = True