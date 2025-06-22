from fastapi import APIRouter

router = APIRouter()

@router.get("/users/me/dietary-records")
async def list_dietary_records():
    pass

@router.get("/users/me/dietary-records/{record_id}")
async def get_dietary_record(record_id: int):
    pass

@router.post("/users/me/dietary-records")
async def save_dietary_record():
    pass

@router.delete("/users/me/dietary-records/{record_id}")
async def delete_dietary_record(record_id: int):
    pass