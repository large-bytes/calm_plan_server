from fastapi import FastAPI, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from . import schemas
from .database import get_db, Base, engine
from sqlalchemy.orm import Session
from .models import Task
from . import models
app = FastAPI()
Base.metadata.create_all(bind=engine)
get_db()

origins = [
    "http://localhost:8000",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/tasks")
async def read_all(db: Session = Depends(get_db)):
    results = db.query(Task).all()
    return results

@app.post("/tasks")
async def add_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    new_task = models.Task(name=task.name, priority=task.priority)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.get("/tasks/{id}")
async def get_task_by_id(id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.delete("/tasks/{id}")
async def delete_task_by_id(id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"ok": True}

@app.put("/tasks/{id}")
async def update_task_by_id(id: int, db: Session = Depends(get_db)):
    # task = db.query(Task).filter(Task.id == id).first()
    # return {"ok": True}
    return task