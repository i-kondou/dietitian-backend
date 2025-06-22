from src.routers import dummy
from fastapi import FastAPI
# import firebase_admin
# from dotenv import load_dotenv
# from firebase_admin.credentials import Certificate

# load_dotenv()


app = FastAPI()

app.include_router(dummy.router, prefix="/dummy", tags=["dummy"])

# cred = Certificate("path/to/your/serviceAccountKey.json")
# firebase_admin.initialize_app(cred)
