from typing import Optional

from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    name: str
    priority: str

class TaskCreate(TaskBase):
    user_id: int


#Task inherits form TaskBase
class Task(TaskBase):
    id: int

class TaskUpdate(BaseModel):
    name: Optional[str] = Field(default=None)
    priority: Optional[str] = Field(default=None)

    class ConfigDict:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    tasks: list[Task] = []

class UserUpdate(BaseModel):
    username: str = Field(default=None)
    email: str = Field(default=None)
    password: str = Field(default=None)

class UserInDB(User):
    hashed_password: str

    class ConfigDict:
        orm_mode = True