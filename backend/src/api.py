from fastapi import FastAPI
from src.routers import meal, user

app = FastAPI()

app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(meal.router, prefix="/meal", tags=["meal"])
