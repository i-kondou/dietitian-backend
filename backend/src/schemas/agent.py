from pydantic import BaseModel, Field

from src.core.enums import Sex

class AgentRequest(BaseModel):
    """エージェントへのリクエスト用"""
    height: float = Field(...)
    weight: float = Field(...)
    age: int = Field(...)
    sex: Sex = Field(...)

class AgentResponse(BaseModel):
    """エージェントの栄養評価レスポンス用"""
    menu: str = Field(..., description="料理の名前")
    calorie: float = Field(0, description="料理の熱量[cal]")
    protein: float = Field(0, description="料理のたんぱく質推定含有量[g]")
    fat: float= Field(0, description="料理の脂質推定含有量[g]")
    carbohydrate: float = Field(0, description="料理の糖質推定含有量[g]")
    dietary_fiber: float = Field(0, description="料理の食物繊維含有量[g]")
    vitamin: float = Field(0, description="料理のビタミン推定含有量[g]")
    mineral: float = Field(0, description="料理のミネラル推定含有量[g]")
    sodium: float = Field(0, description="料理の塩分推定含有量[g]")
    advice_message: str = Field(..., description="昼夜で食べると良い料理の提案や、1日の食生活に関するフィードバック[g]")