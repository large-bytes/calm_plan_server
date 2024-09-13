from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from . import database
from sqlalchemy.orm import Session
from .models import Task
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

@app.get("/tasks")
def read_all(db: Session = Depends(database.get_db)):
    results = db.query(Task).all()
    return results