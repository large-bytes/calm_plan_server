from fastapi import APIRouter
from src.schemas import CreateUserRequest

router = APIRouter()




@router.post("/auth/")
async def create_user():
	return {'user': 'authenticated'}







