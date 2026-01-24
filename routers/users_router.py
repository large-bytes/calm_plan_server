from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src import schemas
from src.database import get_db
from src.models import User
from src.password_utils import hash_password
from src.dependencies import get_current_user

router = APIRouter(
    prefix = '/users',
    tags = ['crud_users']
)

@router.post("")
async def add_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
        hashed_password = hash_password(user.password)
        new_user = User(username=user.username, email=user.email, hashed_password=hashed_password, disabled=False )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

@router.delete("/{user_id}")
async def delete_user_by_id(user_id: int, db: Session = Depends(get_db),  current_user = Depends(get_current_user)):
    print('user')

    if user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    user = db.query(User).filter(User.id == user_id).first()
    print('user',user)
    if not user:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(user)
    db.commit()
    return {"ok": True}

@router.patch("/{user_id}")
async def update_user_by_id(user_id: int, updated_user: schemas.UserUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    if user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    user = db.query(User).filter(User.id == user_id).first()
    user_data = updated_user.model_dump(exclude_unset=True)

    if "password" in user_data:
        user_data["hashed_password"] = hash_password(user_data.pop("password"))

    for k, v in user_data.items():
        setattr(user, k, v)
        print(setattr)
    db.commit()
    db.refresh(user)
    return user
