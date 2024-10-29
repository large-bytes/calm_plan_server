from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from . src import schemas
from . src.models import Base
from . src.database import get_db, engine
from sqlalchemy.orm import Session
from . src.models import Task, User
app = FastAPI()
# Base.metadata.create_all(bind=engine)
get_db()

origins = [
    "http://localhost:8000",
    "http://localhost:5173",
    "https://calmplan.largebytes.co.uk"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/tasks")
async def read_all_tasks(db: Session = Depends(get_db)):
    results = db.query(Task).all()
    return results

@app.post("/tasks")
async def add_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(name=task.name, priority=task.priority)
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

@app.patch("/tasks/{id}")
async def update_task_by_id(id: int, updated_task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    task_data = updated_task.model_dump(exclude_unset=True)
    for k, v in task_data.items():
        setattr(task, k, v)
    db.commit()
    db.refresh(task)
    return task

@app.get("/users")
async def read_all_users(db: Session = Depends(get_db)):
    assert db.query(User).all()

