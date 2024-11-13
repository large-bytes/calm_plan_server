from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src import schemas
from src.database import get_db
from src.models import User

router = APIRouter(
    prefix = '/users',
    tags = ['crud_users']
)

@router.get("")
async def read_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.post("")
async def add_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
        new_user = User(username=user.username, email=user.email, password=user.password, is_active=True )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

@router.get("/{user_id}")
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Task not found")
    return user

@router.delete("/{user_id}")
async def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(user)
    db.commit()
    return {"ok": True}

# @router.patch("/{task_id}")
# async def update_task_by_id(task_id: int, updated_task: schemas.TaskUpdate, db: Session = Depends(get_db)):
#     task = db.query(Task).filter(Task.id == task_id).first()
#     task_data = updated_task.model_dump(exclude_unset=True)
#     for k, v in task_data.items():
#         setattr(task, k, v)
#     db.commit()
#     db.refresh(task)
#     return task