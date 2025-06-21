from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel, Field

# FastAPIのインスタンスを作成
app = FastAPI()

# --- Pydanticモデルの定義 ---
# POSTリクエストで受け取るデータの型を定義


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


# --- APIエンドポイントの定義 ---

@app.post("/", response_model=NutritionResponse)
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
        sodium=0.1
    )
