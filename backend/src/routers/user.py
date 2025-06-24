from fastapi import APIRouter, Depends, HTTPException, status
from google.cloud.firestore_v1.base_document import DocumentSnapshot
from datetime import datetime, timezone
from typing import Any, Mapping, cast
# from src.core.firebase import db
from src.core.deps import get_current_uid, user_doc
from src.schemas.user import ProfileIn, ProfileOut

router = APIRouter()


@router.post("/create", response_model=ProfileOut)
async def create_user(
    uid: str = Depends(get_current_uid)
) -> ProfileOut:
    """ユーザーが存在しない場合は新規にユーザーを作成し、初期状態のプロフィールを返す。
    ユーザーが既に存在する場合は、そのユーザーのプロフィールを返す。

    Args:
        uid (str): ユーザーの一意の識別子。認証システムから取得される。

    Returns:
        ProfileOut: ユーザーのプロフィールデータ。初期状態のプロフィールが作成される場合もある。

    """
    snap: DocumentSnapshot = await user_doc(uid).get()

    if not snap.exists:
        # ユーザーが存在しない場合は初期状態のプロフィールを作成
        initial_profile = ProfileOut(
            uid=uid,
            name="",
            height=0.0,
            weight=0.0,
            sex="male",
            age=0
        )
        await user_doc(uid).set(initial_profile.model_dump() | {"createdAt": datetime.now(timezone.utc)}, merge=True)
        return initial_profile

    data: Mapping[str, Any] = cast(Mapping[str, Any], snap.to_dict() or {})
    return ProfileOut.model_validate({"uid": uid, **data})


@router.post("/update", status_code=status.HTTP_204_NO_CONTENT)
async def update_profile(
    body: ProfileIn,
    uid: str = Depends(get_current_uid)
) -> None:
    """ユーザーのプロフィールデータを更新する。

    Args:
        body (ProfileIn): 更新するプロフィールデータ。身長、体重、性別、年齢などを含む。
        uid (str): ユーザーの一意の識別子。認証システムから取得される。

    Returns:
        None: このエンドポイントはコンテンツを返さない。成功時には204 No Content ステータスを返す。

    """

    await user_doc(uid).set(
        body.model_dump() | {"updatedAt": datetime.now(timezone.utc)},
        merge=True
    )


@router.get("/read", response_model=ProfileOut)
async def get_profile(uid: str = Depends(get_current_uid)) -> ProfileOut:
    """ユーザーのプロフィールデータを Firestore から取得する。

    Args:
        uid (str): ユーザーの一意の識別子。認証システムから取得される。

    Returns:
        ProfileOut: ユーザーのプロフィールデータ。身長、体重、性別、年齢などを含む。

    """
    snap: DocumentSnapshot = await user_doc(uid).get()

    if not snap.exists:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Profile not found")

    data: Mapping[str, Any] = cast(Mapping[str, Any], snap.to_dict() or {})

    return ProfileOut.model_validate({"uid": uid, **data})
