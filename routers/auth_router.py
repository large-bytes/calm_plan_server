from fastapi import APIRouter
from typing_extensions import deprecated

from src.schemas import CreateUserRequest
from src.models import User
from passlib.context import CryptContext

router = APIRouter()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

@router.post("/auth")
async def create_user(create_user_request: CreateUserRequest):
	create_user_model = User(
		username=create_user_request.username,
		email=create_user_request.email,
		role=create_user_request.role,
		hashed_password=bcrypt_context.hash(create_user_request.password),
		is_active=True
	)

	return create_user_model





