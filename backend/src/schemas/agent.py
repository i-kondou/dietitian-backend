from pydantic import BaseModel, Field

from src.core.enums import Sex

class AgentRequest(BaseModel):
    """エージェントへのリクエスト用"""
    height: float = Field(..., description="身長 [cm]")
    weight: float = Field(..., description="体重 [kg]")
    age: int = Field(..., description="年齢 [歳]")
    sex: Sex = Field(..., description="性別 [男性 or 女性]")

class AgentResponse(BaseModel):
    """エージェントの栄養評価レスポンス用"""
    menu: str = Field(..., description="料理の名前")
    calorie: float = Field(..., description="料理の熱量[cal]")
    protein: float = Field(..., description="料理のたんぱく質推定含有量[g]")
    fat: float= Field(..., description="料理の脂質推定含有量[g]")
    carbohydrate: float = Field(..., description="料理の糖質推定含有量[g]")
    dietary_fiber: float = Field(..., description="料理の食物繊維含有量[g]")
    vitamin: float = Field(..., description="料理のビタミン推定含有量[g]")
    mineral: float = Field(..., description="料理のミネラル推定含有量[g]")
    sodium: float = Field(..., description="料理の塩分推定含有量[g]")
    advice_message: str = Field(..., description="昼夜で食べると良い料理の提案や、1日の食生活に関するフィードバック[g]")