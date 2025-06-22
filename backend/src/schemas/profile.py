from pydantic import BaseModel, Field


class ProfileIn(BaseModel):
    """Profile data input by the user, including height, weight, sex, and age.
    """
    height: int = Field(..., ge=50, le=300)
    weight: float = Field(..., gt=0)
    sex: str = Field(..., pattern="^(male|female|other)$")
    age: int = Field(..., ge=0, le=120)


class ProfileOut(ProfileIn):
    """Profile data returned to the client, including the user's unique identifier.
    """
    uid: str
