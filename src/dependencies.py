from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from src.database import get_db
from src.models import User
from src.jwt_utils import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = decode_access_token(token)
    except Exception:
        HTTPException(status_code=401, detail="Invalid token")

    payload = decode_access_token(token)
    user_id = payload["sub"]
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code = 401, detail="Invalid user")
    return user 
