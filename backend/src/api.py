from src.routers import dummy
from fastapi import FastAPI
import firebase_admin
from firebase_admin.credentials import Certificate

cred_path = "/secrets/firebase-adminsdk.json"


app = FastAPI()

app.include_router(dummy.router, prefix="/dummy", tags=["dummy"])

cred = Certificate(cred_path)
firebase_admin.initialize_app(cred)
