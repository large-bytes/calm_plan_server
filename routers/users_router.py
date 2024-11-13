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
