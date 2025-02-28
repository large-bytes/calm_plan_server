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

# new jwt imports

# router = APIRouter(
#     prefix = '/auth',
#     tags = ['authentication']
# )

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
db = get_db()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)  

def get_password_hash(password):
    return pwd_context.hash(password)
    
def get_user(username:str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise ValueError(f"User with username '{username}' not found'")
    user_dict = {key: value for key, value in user.__dict__.items() if not key.startswith("_")}
    return UserInDB.model_validate(user_dict)

def authenticate_user(username:str, password:str,  db: Session = Depends(get_db)):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user



def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes = 15)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(username=token_data.username  , db=db)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
        current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

#todo understand from this point down
@app.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db) ) -> Token:
    user = authenticate_user(form_data.username, form_data.password, db = db,)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers = {"WWW-Authenticate": "Bearer"},
        )


    access_token_expires = timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta= access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@app.get("/me")
async def read_users_me(
        current_user: Annotated[User, Depends(get_current_active_user)],
        ):
    return current_user

@app.get("/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]


if __name__ == "__main__":
    db_session = next(get_db())

    username = "test1"

    try:
        user_data = get_user(username, db_session)
        print("Returned User Object:", user_data)
    except Exception as e:
            print(f"Error: {e}")

