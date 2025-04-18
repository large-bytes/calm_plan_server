from fastapi import APIRouter
from src.schemas import CreateUserRequest
from src.models import User

router = APIRouter()




@router.post("/auth/")
async def create_user(create_user_request: CreateUserRequest):
	create_user_model = User(
		username=create_user_request.username,
		email=create_user_request.email,
		role=create_user_request.role,
		hashed_password=create_user_request.password,
		is_active=True
	)

	return create_user_model





