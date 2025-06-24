from __future__ import annotations
import os
import firebase_admin
from firebase_admin.credentials import Certificate
from firebase_admin import firestore_async

cred_path = os.getenv("FIREBASE_ADMINSDK_JSON",
                      "/secrets/firebase-adminsdk.json")

default_app = firebase_admin.initialize_app(Certificate(cred_path))

db = firestore_async.client(app=default_app)
