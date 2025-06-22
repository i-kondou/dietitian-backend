from fastapi import APIRouter, Depends, HTTPException, status
from google.cloud.firestore_v1.async_document import AsyncDocumentReference
from google.cloud.firestore_v1.base_document import DocumentSnapshot
from datetime import datetime
from typing import Any, Mapping, cast
from src.core.firebase import db
from src.core.deps import get_current_uid
from src.schemas.profile import ProfileIn, ProfileOut

router = APIRouter()


def user_doc(uid: str) -> AsyncDocumentReference:
    """Get a reference to the user's document in Firestore.

    Args:
        uid (str): The unique identifier of the user.

    Returns:
        AsyncDocumentReference: A reference to the user's document in the Firestore database.

    """
    return db.collection("users").document(uid)


@router.post("", status_code=status.HTTP_204_NO_CONTENT)
async def upsert_profile(
    body: ProfileIn,
    uid: str = Depends(get_current_uid)
) -> None:
    """Upsert the user's profile data in Firestore.
    If the user does not exist, create a new document. If the user exists,
    update the existing document with the provided data.

    Args:
        body (ProfileIn): The profile data to be upserted.
        uid (str): The unique identifier of the user, obtained from the authentication system.

    Returns:
        None: This endpoint does not return any content.

    """
    await user_doc(uid).set(
        body.model_dump() | {"updatedAt": datetime.utcnow()}, merge=True
    )


@router.get("", response_model=ProfileOut)
async def get_profile(uid: str = Depends(get_current_uid)) -> ProfileOut:
    """Retrieve the user's profile data from Firestore.

    Args:
        uid (str): The unique identifier of the user, obtained from the authentication system.

    Returns:
        ProfileOut: The user's profile data, including height and weight.

    """
    snap: DocumentSnapshot = await user_doc(uid).get()

    if not snap.exists:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Profile not found")

    data: Mapping[str, Any] = cast(Mapping[str, Any], snap.to_dict() or {})
    # Pydantic v2 なら model_validate が便利
    return ProfileOut.model_validate({"uid": uid, **data})
