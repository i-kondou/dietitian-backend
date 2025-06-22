from fastapi import FastAPI
import firebase_admin
from firebase_admin.credentials import Certificate

from src.routers import dummy

app = FastAPI()

app.include_router(dummy.router, prefix="/dummy", tags=["dummy"])

cred = Certificate("path/to/your/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
