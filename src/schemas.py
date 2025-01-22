from typing import Optional, List
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
        from_attributes = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    hashed_password: str

class User(UserBase):
    id: int
    disabled: bool
    tasks: List[dict] = []

    class ConfigDict:
        from_attributes = True


class UserInDB(User):
    hashed_password: str

    class ConfigDict:
        from_attributes = True