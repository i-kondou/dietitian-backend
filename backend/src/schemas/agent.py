from pydantic import BaseModel, Field

class AgentRequest(BaseModel):
    """エージェントへのリクエスト用"""
    image_url: str = Field(..., description="料理画像のFirebase上URL")

class AgentResponse(BaseModel):
    """エージェントの栄養評価レスポンス用"""
    calorie: float = Field(0, description="料理の熱量")
    protein: float = Field(0, description="料理のたんぱく質推定含有量")
    fat: float= Field(0, description="料理の脂質推定含有量")
    carbohydrate: float = Field(0, description="料理の炭水化物推定含有量")
    dietary_fiber: float = Field(0, description="料理の食物繊維含有量")
    vitamin: float = Field(0, description="料理のビタミン推定含有量")
    mineral: float = Field(0, description="料理のミネラル推定含有量")
    sodium: float = Field(0, description="料理の塩分推定含有量")
    content: str = Field(..., description="昼夜で食べると良い料理の提案や、1日の食生活に関するフィードバック")