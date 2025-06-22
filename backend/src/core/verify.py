from fastapi import HTTPException, status, Request
from firebase_admin.auth import verify_id_token

def verify_token(request: Request) -> str:
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="認証情報がありません。")
    
    id_token = auth_header.split(" ")[1]

    try:
        decoded_token = verify_id_token(id_token=id_token)
        uid = decoded_token["uid"]
        return uid
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="トークンの検証に失敗しました")