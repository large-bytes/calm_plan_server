from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from database  import get_db
from models import Task
from sqlalchemy.orm import Session

app = FastAPI()

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/tasks_list")
# async def tasks_list():
#     return {"all_tasks": task_list }

@app.get("/tasks")
def read_all(db: Session = Depends(get_db)):
    return db