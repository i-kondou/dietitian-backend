import typing
from langchain_core.messages import HumanMessage
from src.core.nutrition_advice_agent.common import vision_llm, as_image_part
from src.schemas.meal import NutrientList, Nutrient


def get_nutrition(image_src: str, dishes: list[str]) -> list[Nutrient]:
    """画像と料理名リストを基に、各料理の栄養素を推定する。

    Args:
        image_src (str): 料理の画像 URL
        dishes (list[str]): 料理名のリスト

    Returns:
        list[Nutrient]: 各料理の栄養素リスト

    """
    prompt = (
        "画像と料理名リストを参考に、各料理の概算栄養素を JSON で返してください。"
        "単位は kcal と g で統一してください。"
        """
        これらは必ず含めてください:
        - dish: 料理名
        - calorie: 料理のカロリー[cal]
        - protein: 料理のタンパク質推定含有量[g]
        - fat: 料理の脂質推定含有量[g]
        - carbohydrate: 料理の炭水化物推定含有量[g]
        - dietary_fiber: 料理の食物繊維推定含有量[g]
        - vitamin: 料理のビタミン推定含有量[g]
        - mineral: 料理のミネラル推定含有量[g]
        - sodium: 料理の塩分推定含有量[g]
        """
    )
    llm = vision_llm.with_structured_output(NutrientList)
    msg = HumanMessage(
        content=[
            {
                "type": "text",
                "text": prompt + f"\n料理名リスト: {', '.join(dishes)}"
            },
            as_image_part(image_src),
        ]
    )

    response = typing.cast(NutrientList, llm.invoke([msg]))
    return response.nutrients
