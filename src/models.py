from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

#USER MODEL CLASS -
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String(60))
    is_active = Column(Boolean, default=True)
    role = Column(String)

    task = relationship("Task", back_populates="user")

    def __repr__(self):
        return f"id:{self.id}, username: {self.username}"


# TASK MODEL CLASS -
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    priority = Column(String, index=True)
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="task")

    def __repr__(self):
        return f"id:{self.id}, name: {self.username}, priority: {self.prority}"


