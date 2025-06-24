from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from google.cloud.firestore_v1.async_document import AsyncDocumentReference
from src.core.firebase import db
from starlette.concurrency import run_in_threadpool
from firebase_admin import auth


bearer_scheme = HTTPBearer(auto_error=True)


async def get_current_uid(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)  # noqa: B008
) -> str:
    """Get the current user's UID from the Firebase ID token.

    Args:
        credentials (HTTPAuthorizationCredentials): The credentials provided by the user,
            typically in the form of a Bearer token.

    Returns:
        str: The UID of the authenticated user.

    """
    id_token = credentials.credentials

    try:
        decoded = await run_in_threadpool(auth.verify_id_token, id_token)
        return decoded["uid"]
    except Exception as err:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                            f"Token verification failed: {err}") from err


def user_doc(uid: str) -> AsyncDocumentReference:
    """Firestore のユーザードキュメントへの参照を取得する。

    Args:
        uid (str): ユーザーの一意の識別子。

    Returns:
        AsyncDocumentReference: Firestore データベース内のユーザードキュメントへの参照。

    """
    return db.collection("users").document(uid)
