from pydantic import BaseModel, Field
from typing import Optional

from src.core.enums import Sex

class UserCreate(BaseModel):
    name: str = Field(...)
    height: float = Field(..., description="身長 [cm]")
    weight: float = Field(..., description="体重 [kg]")
    age: int = Field(..., description="年齢 [歳]")
    sex: Sex = Field(..., description="性別 [男性 or 女性]")

class UserUpdate(BaseModel):
    name: Optional[str] = Field(None)
    height: Optional[float] = Field(None, description="身長 [cm]")
    weight: Optional[float] = Field(None, description="体重 [kg]")
    age: Optional[int] = Field(None, description="年齢 [歳]")
    sex: Optional[Sex] = Field(None, description="性別 [男性 or 女性]")

class UserResponse(UserCreate):
    pass