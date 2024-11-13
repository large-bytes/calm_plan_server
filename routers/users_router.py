from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src import schemas
from src.database import get_db
from src.models import User

router = APIRouter(
    prefix = '/users',
    tags = ['crud_users']
)

@router.get("")
async def read_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.post("")
async def add_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
        new_user = User(username=user.username, email=user.email, password=user.password, is_active=True )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user