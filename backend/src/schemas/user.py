from pydantic import BaseModel, Field
from typing import Optional

from src.core.enums import Sex

class UserCreate(BaseModel):
    name: str = Field(...)
    height: float = Field(...)
    weight: float = Field(...)
    age: int = Field(...)
    sex: Sex = Field(...)

class UserUpdate(BaseModel):
    name: Optional[str] = Field(None)
    height: Optional[float] = Field(None)
    weight: Optional[float] = Field(None)
    age: Optional[int] = Field(None)
    sex: Optional[Sex] = Field(None)

class UserResponse(UserCreate):
    pass