import jwt
from jose.constants import ALGORITHMS
from jwt import InvalidTokenError

from src.database import get_db

from src.schemas import UserInDB, TokenData, Token
from src.models import User
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, status
from typing import Annotated
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv
import os

from passlib.context import CryptContext

load_dotenv()
from routers import auth_router, tasks_router, users_router

app = FastAPI()
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


app.include_router(tasks_router.router)
app.include_router(users_router.router)

# #auth router
app.include_router(auth_router.router)


