from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src import schemas
from src.database import get_db
from src.models import Task

router = APIRouter(
    prefix = '/tasks',
    tags = ['crud_tasks']
)

@router.get("")
async def read_all_tasks(db: Session = Depends(get_db)):
    results = db.query(Task).all()
    return results

@router.post("")
async def add_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(name=task.name, priority=task.priority)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/{id}")
async def get_task_by_id(id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{id}")
async def delete_task_by_id(id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"ok": True}

@router.patch("/{id}")
async def update_task_by_id(id: int, updated_task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    task_data = updated_task.model_dump(exclude_unset=True)
    for k, v in task_data.items():
        setattr(task, k, v)
    db.commit()
    db.refresh(task)
    return task

