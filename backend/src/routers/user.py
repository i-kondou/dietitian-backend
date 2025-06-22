from fastapi import APIRouter, Request, Depends

from src.core.verify import verify_token
import src.schemas.user as user_schema

router = APIRouter()

@router.get("/users/me")
async def get_user_info():
    pass

@router.post("/users/me/register", response_model=user_schema.UserResponse)
async def register_user(user_create: user_schema.UserCreate, uid: str = Depends(verify_token)):
    return user_schema.UserResponse(**user_create.dict())

@router.put("/users/me")
async def update_user_info():
    pass

@router.delete("/users/me")
async def delete_account():
    pass