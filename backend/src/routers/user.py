from fastapi import APIRouter

router = APIRouter()

@router.get("/users/me")
async def get_user_info():
    pass

@router.post("/users/me/register")
async def register_user():
    pass

@router.put("/users/me")
async def update_user_info():
    pass

@router.delete("/users/me")
async def delete_account():
    pass