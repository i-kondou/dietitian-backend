from fastapi import Header, HTTPException, status
from starlette.concurrency import run_in_threadpool
from firebase_admin import auth


async def get_current_uid(
    authorization: str = Header(..., description="Bearer <Firebase ID token>")
) -> str:
    """Get the current user's UID from the Firebase ID token.

    Args:
        authorization (str): The Authorization header containing the Bearer token.

    Returns:
        str: The UID of the authenticated user.

    """
    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer":
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                            "Invalid auth header")

    try:
        decoded = await run_in_threadpool(auth.verify_id_token, token)
        return decoded["uid"]
    except Exception as err:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                            f"Token verification failed: {err}") from err
