from fastapi import FastAPI
from src.routers import user

app = FastAPI()

app.include_router(user.router, prefix="/user", tags=["user"])
# app.include_router(agent.router, prefix="/agent", tags=["agent"])
