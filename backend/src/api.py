from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

from src.routers import agent
from src.routers import dietary_record
from src.routers import user

# FastAPIのインスタンスを作成
app = FastAPI()

app.include_router(agent.router)
app.include_router(dietary_record.router)
app.include_router(user.router)