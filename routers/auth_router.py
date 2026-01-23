from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.database import get_db
from src.models import User
from src.password_utils import verify_password
from src.jwt_utils import create_access_token
from src.dependencies import get_current_user



router = APIRouter()

@router.post("/auth/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    login_username = form_data.username
    login_password = form_data.password
    user = db.query(User).filter(User.username == login_username).first()
    
    if not user or not verify_password(login_password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({'sub': str(user.id)})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/auth/me")
async def get_me(current_user = Depends(get_current_user)):
    return current_user








