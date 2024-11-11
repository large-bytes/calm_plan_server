from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from . import tasks_router
from . src import schemas
from . src.models import Base
from . src.database import get_db, engine
from sqlalchemy.orm import Session
from . src.models import Task, User

app = FastAPI()

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

#tasks router
app.include_router(tasks_router.router)


@app.get("/users")
async def read_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()

