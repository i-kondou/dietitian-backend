from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, status
import firebase_admin
from firebase_admin.credentials import Certificate
import os

from src.routers import agent
from src.routers import dietary_record
from src.routers import user

# FastAPIのインスタンスを作成
app = FastAPI()

app.include_router(agent.router)
app.include_router(dietary_record.router)
app.include_router(user.router)

load_dotenv()

cred_path = os.environ.get("FIREBASE_CREDENTIAL_PATH")
if cred_path:
    cred = Certificate(cred_path)
else:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="FIREBASE_CREDENTIAL_PATHが設定されていません。")

firebase_admin.initialize_app(cred)