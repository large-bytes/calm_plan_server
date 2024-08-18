from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from . import models, schemas 
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
# from typing import List, Annotated
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
        
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

test_tasks_db= [
        {"id": "1", "name": "Learn JavaScript", "priority": "five"},
        {"id": "2", "name": "Deploy app", "priority": "five"},
        {"id": "3", "name": "Update project dependencies", "priority": "three"},
        {"id": "4", "name": "Write docs", "priority": "two"},
        {"id": "5", "name": "Refactor app.js", "priority": "one"},
    ]


@app.get("/tasks")
async def read_item():
    return {"all_tasks": test_tasks_db }

