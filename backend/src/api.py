from src.routers import profile
from fastapi import FastAPI

app = FastAPI()

app.include_router(profile.router, prefix="/profile", tags=["profile"])
