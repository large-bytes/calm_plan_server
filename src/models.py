from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# #USER MODEL CLASS -
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(10), nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String(8), nullable=False)
    is_active = Column(Boolean, default=True)

    tasks = relationship("Task", back_populates="user")

    def __repr__(self):
        return f"id:{self.id}, username: {self.username}"


# TASK MODEL CLASS -
# class Task(Base):
#     __tablename__ = "tasks"
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String, index=True)
#     priority = Column(String, index=True)
#     # user_id = Column(Integer, ForeignKey("users.id"))
#
#     user = relationship("User", back_populates="tasks")
#
#     def __repr__(self):
#         return f"id:{self.id}, name: {self.username}, priority: {self.prority}"
#     __table_args__ = {'extend_existing': True}
#

