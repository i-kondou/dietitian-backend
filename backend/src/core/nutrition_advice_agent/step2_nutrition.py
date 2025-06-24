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
        "フィールドには、料理名を示す文字列**だけ**を含めてください。例: `うどん`"
        "`dish`フィールドに`dish=`のような余分なテキストを含めないでください。"
    )
    llm = vision_llm.with_structured_output(NutrientList)
    msg = HumanMessage(content=[
        {"type": "text", "text": prompt + f"\n料理名リスト: {', '.join(dishes)}"},
        as_image_part(image_src),
    ])

    response = typing.cast(NutrientList, llm.invoke([msg]))
    return response.nutrients
