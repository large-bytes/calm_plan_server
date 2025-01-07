from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


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

#tasks router
app.include_router(tasks_router.router)

#users router
app.include_router(users_router.router)

# #auth router
# app.include_router(auth_router.router)

from http.client import HTTPException

from sqlalchemy.sql.functions import current_user
from src.database import get_db

from src.schemas import User, UserInDB
# from src.models import User

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, status
from typing import Annotated

from sqlalchemy.orm import Session

# router = APIRouter(
#     prefix = '/auth',
#     tags = ['authentication']
# )

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def fake_hashed_password(password: str):
    return "fakehashed" + password


def get_user(username:str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    user_dict = {key: value for key, value in user.__dict__.items() if not key.startswith("_")}
    return UserInDB(user_dict)

def fake_decode_token(token, db: Session = Depends(get_db)):
    user = get_user(token, db)
    return user

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return user

async def get_current_active_user(
        current_user: Annotated[User, Depends(get_current_user)]
):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db) ):
    user = db.query(User).filter(User.username == form_data.username).first()
    user_dict = {key: value for key, value in user.__dict__.items() if not key.startswith("_")}
    print("hello")
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(user_dict)
    hashed_password =  fake_hashed_password(form_data.password)
    if not hashed_password == user.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/me")
async def read_users_me(
        current_user: Annotated[User, Depends(get_current_active_user)],
        ):
    return current_user


