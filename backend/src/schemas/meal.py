from datetime import datetime
from pydantic import BaseModel, Field


class Dish(BaseModel):
    """料理名を表すモデル。

    Attributes:
        dish (str): 料理名

    """
    dish: str = Field(..., min_length=1, max_length=100, description="料理名")


class DishList(BaseModel):
    """料理名のリストを表すモデル。

    Attributes:
        dishes (list[Dish]): 料理名のリスト

    """
    dishes: list[Dish] = Field(..., description="料理名のリスト")


class Nutrient(BaseModel):
    """料理の栄養素情報を表すモデル。

    Attributes:
        dish (str): 料理名
        calorie (float): 料理のカロリー[cal]
        protein (float): 料理のタンパク質推定含有量[g]
        fat (float): 料理の脂質推定含有量[g]
        carbohydrate (float): 料理の炭水化物推定含有量[g]
        dietary_fiber (float): 料理の食物繊維推定含有量[g]
        vitamin (float): 料理のビタミン推定含有量[g]
        mineral (float): 料理のミネラル推定含有量[g]
        sodium (float): 料理の塩分推定含有量[g]

    """
    dish: str = Field(..., description="料理名")
    calorie: float = Field(..., ge=0, description="料理のカロリー[cal]")
    protein: float = Field(..., ge=0, description="料理のタンパク質推定含有量[g]")
    fat: float = Field(..., ge=0, description="料理の脂質推定含有量[g]")
    carbohydrate: float = Field(..., ge=0, description="料理の炭水化物推定含有量[g]")
    dietary_fiber: float = Field(..., ge=0, description="料理の食物繊維推定含有量[g]")
    vitamin: float = Field(..., ge=0, description="料理のビタミン推定含有量[g]")
    mineral: float = Field(..., ge=0, description="料理のミネラル推定含有量[g]")
    sodium: float = Field(..., ge=0, description="料理の塩分推定含有量[g]")


class NutrientList(BaseModel):
    """料理の栄養素情報のリストを表すモデル。

    Attributes:
        nutrients (list[Nutrient]): 料理の栄養素情報のリスト

    """
    nutrients: list[Nutrient] = Field(
        ..., description="料理の栄養素情報のリスト")


class DishUrl(BaseModel):
    """料理の画像URLを表すモデル。

    Attributes:
        imageUrl (str): 料理の画像URL

    """
    imageUrl: str = Field(..., description="料理の画像URL")


class BodyInfo(BaseModel):
    """ユーザーの身体情報を表すモデル。

    Attributes:
        height (float): ユーザーの身長[cm]
        weight (float): ユーザーの体重[kg]
        age (int): ユーザーの年齢[歳]
        sex (str): ユーザーの性別 [男性 or 女性]

    """
    height: float = Field(..., gt=0, description="ユーザーの身長[cm]")
    weight: float = Field(..., gt=0, description="ユーザーの体重[kg]")
    age: int = Field(..., ge=0, le=120, description="ユーザーの年齢[歳]")
    sex: str = Field(..., description="ユーザーの性別 [男性 or 女性]")


class Advice(BaseModel):
    """栄養に関するアドバイスを表すモデル。

    Attributes:
        advice (str): 栄養に関するアドバイスメッセージ

    """
    advice: str = Field(..., description="栄養に関するアドバイスメッセージ")


class MealUploadResponse(BaseModel):
    """料理の栄養情報とアドバイスを含むレスポンスモデル。

    Attributes:
        menu_name (str): 料理の名前
        calorie (float): 料理のカロリー[cal]
        protein (float): 料理のタンパク質推定含有量[g]
        fat (float): 料理の脂質推定含有量[g]
        carbohydrate (float): 料理の炭水化物推定含有量[g]
        dietary_fiber (float): 料理の食物繊維推定含有量[g]
        vitamin (float): 料理のビタミン推定含有量[g]
        mineral (float): 料理のミネラル推定含有量[g]
        sodium (float): 料理の塩分推定含有量[g]
        advice_message (str): 料理に関するアドバイスメッセージ

    """
    menu_name: str = Field(..., min_length=1,
                           max_length=100, description="料理の名前")
    calorie: float = Field(..., ge=0, description="料理のカロリー[cal]")
    protein: float = Field(..., ge=0, description="料理のタンパク質推定含有量[g]")
    fat: float = Field(..., ge=0, description="料理の脂質推定含有量[g]")
    carbohydrate: float = Field(..., ge=0, description="料理の炭水化物推定含有量[g]")
    dietary_fiber: float = Field(..., ge=0, description="料理の食物繊維推定含有量[g]")
    vitamin: float = Field(..., ge=0, description="料理のビタミン推定含有量[g]")
    mineral: float = Field(..., ge=0, description="料理のミネラル推定含有量[g]")
    sodium: float = Field(..., ge=0, description="料理の塩分推定含有量[g]")
    advice_message: str = Field(..., description="料理に関するアドバイスメッセージ")


class MealInput(BaseModel):
    """料理の栄養情報とアドバイスを含む入力モデル。

    Attributes:
        imageUrl (str): 料理の画像URL
        menu_name (str): 料理の名前
        calorie (float): 料理のカロリー[cal]
        protein (float): 料理のタンパク質推定含有量[g]
        fat (float): 料理の脂質推定含有量[g]
        carbohydrate (float): 料理の炭水化物推定含有量[g]
        dietary_fiber (float): 料理の食物繊維推定含有量[g]
        vitamin (float): 料理のビタミン推定含有量[g]
        mineral (float): 料理のミネラル推定含有量[g]
        sodium (float): 料理の塩分推定含有量[g]
        advice_message (str): 料理に関するアドバイスメッセージ

    """
    imageUrl: str = Field(..., description="料理の画像URL")
    menu_name: str = Field(..., min_length=1,
                           max_length=100, description="料理の名前")
    calorie: float = Field(..., ge=0, description="料理のカロリー[cal]")
    protein: float = Field(..., ge=0, description="料理のタンパク質推定含有量[g]")
    fat: float = Field(..., ge=0, description="料理の脂質推定含有量[g]")
    carbohydrate: float = Field(..., ge=0, description="料理の炭水化物推定含有量[g]")
    dietary_fiber: float = Field(..., ge=0, description="料理の食物繊維推定含有量[g]")
    vitamin: float = Field(..., ge=0, description="料理のビタミン推定含有量[g]")
    mineral: float = Field(..., ge=0, description="料理のミネラル推定含有量[g]")
    sodium: float = Field(..., ge=0, description="料理の塩分推定含有量[g]")
    advice_message: str = Field(..., description="料理に関するアドバイスメッセージ")

class MealRecord(MealInput):
    """料理の画像URL、栄養情報、アドバイスを含むストレージ取り出し用モデル。

    Attributes:
        imageUrl (str): 料理の画像URL
        menu_name (str): 料理の名前
        calorie (float): 料理のカロリー[cal]
        protein (float): 料理のタンパク質推定含有量[g]
        fat (float): 料理の脂質推定含有量[g]
        carbohydrate (float): 料理の炭水化物推定含有量[g]
        dietary_fiber (float): 料理の食物繊維推定含有量[g]
        vitamin (float): 料理のビタミン推定含有量[g]
        mineral (float): 料理のミネラル推定含有量[g]
        sodium (float): 料理の塩分推定含有量[g]
        advice_message (str): 料理に関するアドバイスメッセージ
        eaten_at (datetime): 料理がFirestoreに記録された時刻

    """
    eaten_at: datetime = Field(..., alias="eatenAt", description="料理がFirestoreに記録された時刻")

    # aliasを有効化(Firestore上ではeatenAt、FastAPIではeaten_at)
    model_config = {
        "populate_by_name": True
    }

class MealRecordList(BaseModel):
    """料理の画像URL、栄養情報、アドバイスのリストを表すモデル。

    Attributes:
        mealRecords (list[MealRecord]): 料理の画像URL、栄養情報、アドバイスのリスト

    """
    meal_records: list[MealRecord] = Field(..., description="料理の画像URL、栄養情報、アドバイスのリスト")
