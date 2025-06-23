from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.concurrency import run_in_threadpool
from firebase_admin import auth


bearer_scheme = HTTPBearer(auto_error=True)


async def get_current_uid(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)
) -> str:
    """Get the current user's UID from the Firebase ID token.

    Args:
        authorization (str): The Authorization header containing the Bearer token.

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
