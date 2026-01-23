from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src import schemas
from src.database import get_db
from src.models import Task
from src.dependencies import get_current_user

router = APIRouter(
    prefix = '/tasks',
    tags = ['crud_tasks']
)

@router.get("")
async def read_all_tasks(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    results = db.query(Task).filter(Task.user_id == current_user.id).all()
    return results

@router.post("")
async def add_task(task: schemas.TaskCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):    
    new_task = Task(name=task.name, priority=task.priority, user_id=current_user.id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/{task_id}")
async def get_task_by_id(task_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{id}")
async def delete_task_by_id(id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == id, Task.user_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"ok": True}

@router.patch("/{task_id}")
async def update_task_by_id(task_id: int, updated_task: schemas.TaskUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
    task_data = updated_task.model_dump(exclude_unset=True)
    for k, v in task_data.items():
        setattr(task, k, v)
    db.commit()
    db.refresh(task)
    return task

