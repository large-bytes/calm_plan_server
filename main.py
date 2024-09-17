from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, get_db, engine
from sqlalchemy.orm import Session
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
def read_all(db: Session = Depends(get_db)):
    results = db.query(models.Task).all()
    return results