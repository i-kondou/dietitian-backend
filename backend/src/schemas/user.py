from pydantic import BaseModel, Field


class ProfileIn(BaseModel):
    """Profile data input by the user, including height, weight, sex, and age.
    """
    name: str = Field(..., min_length=1, max_length=100)
    height: float = Field(..., ge=50, le=300)
    weight: float = Field(..., gt=0)
    sex: str = Field(..., pattern="^(男性|女性)$")
    age: int = Field(..., ge=0, le=120)


class ProfileOut(ProfileIn):
    """Profile data returned to the client, including the user's unique identifier.
    """
    uid: str
