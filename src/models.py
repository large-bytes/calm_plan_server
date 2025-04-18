from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# #USERS MODEL CLASS -
class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String(225))
    is_active = Column(Boolean, default=True)
    role = Column(String)

    tasks = relationship("Task", back_populates="user")

    def __repr__(self):
        return f"id:{self.id}, username: {self.username}"


# TASKS MODEL CLASS -
class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    priority = Column(String, index=True)
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    users = relationship("User", back_populates="tasks")

    def __repr__(self):
        return f"id:{self.id}, name: {self.username}, priority: {self.prority}"
    __table_args__ = {'extend_existing': True}


