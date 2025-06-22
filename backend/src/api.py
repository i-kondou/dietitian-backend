from fastapi import FastAPI
import firebase_admin
from firebase_admin.credentials import Certificate

from src.routers import agent
from src.routers import dietary_record
from src.routers import user

# FastAPIのインスタンスを作成
app = FastAPI()

app.include_router(agent.router)
app.include_router(dietary_record.router)
app.include_router(user.router)

# TODO: firebase-adminsdk.jsonのパス入れる(json自体はどっかに置いてgitignoreに記載)
cred = Certificate("")
firebase_admin.initialize_app(cred)