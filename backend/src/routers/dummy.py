from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel, Field

router = APIRouter()


class User(BaseModel):
    """ユーザーモデル。

    Attributes:
        id_token (str): ユーザーIDトークン

    """
    id_token: str = Field(..., description="ユーザーIDトークン")


class UserInfo(User):
    """ユーザー情報モデル。

    Attributes:
        name (str): ユーザー名
        height (float): 身長 (cm)
        weight (float): 体重 (kg)
        age (int): 年齢 (歳)
        sex (str): 性別

    """
    name: str = Field(..., description="ユーザー名")
    height: float = Field(..., description="身長 (cm)")
    weight: float = Field(..., description="体重 (kg)")
    age: int = Field(..., description="年齢 (歳)")
    sex: str = Field(..., description="性別")


class NutritionResponse(BaseModel):
    """
    食品の栄養成分を表すモデル。
    Attributes:
        menu (str): 食品名
        calorie (float): カロリー
        protein (float): タンパク質
        fat (float): 脂質
        carbohydrate (float): 炭水化物
        dietary_fiber (float): 食物繊維
        vitamin (float): ビタミン
        mineral (float): ミネラル
        sodium (float): ナトリウム
    """
    menu: str = Field(..., description="食品名")
    calorie: float = Field(..., description="カロリー")
    protein: float = Field(..., description="タンパク質")
    fat: float = Field(..., description="脂質")
    carbohydrate: float = Field(..., description="炭水化物")
    dietary_fiber: float = Field(..., description="食物繊維")
    vitamin: float = Field(..., description="ビタミン")
    mineral: float = Field(..., description="ミネラル")
    sodium: float = Field(..., description="ナトリウム")
    advice_message: str = Field(..., description="アドバイスメッセージ",
                                default="This is a mock response. Please implement actual logic.")


# --- APIエンドポイントの定義 ---

@router.post("/nutrition", response_model=NutritionResponse)
def nutrition_process_mock(file: UploadFile = File(...)) -> NutritionResponse:  # noqa: B008
    """Mock API endpoint to process a file and return nutrition information.

    Args:
        file (UploadFile): アップロードされたファイル

    Returns:
        NutritionResponse: 栄養成分の情報を含むレスポンス

    """
    if not file:
        raise ValueError()

    return NutritionResponse(
        menu="Example Food",
        calorie=100.0,
        protein=5.0,
        fat=2.0,
        carbohydrate=20.0,
        dietary_fiber=3.0,
        vitamin=1.0,
        mineral=0.5,
        sodium=0.1,
        advice_message="This is a mock response. Please implement actual logic."
    )


@router.post("/user/register", response_model=User)
def user_register(user: User) -> User:
    """Register a user.

    Args:
        user (User): ユーザー情報

    Returns:
        User: 登録されたユーザー情報

    """

    if not user.id_token:
        raise ValueError()
    return user


@router.post("/user/update", response_model=UserInfo)
def user_info_register(user_info: UserInfo) -> UserInfo:
    """Register user information.

    Args:
        user_info(UserInfo): ユーザー情報

    Returns:
        UserInfo: 登録されたユーザー情報

    """
    if not user_info.id_token:
        raise ValueError()
    return user_info
