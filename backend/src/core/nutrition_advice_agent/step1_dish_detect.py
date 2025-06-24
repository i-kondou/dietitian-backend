import typing
from langchain_core.messages import HumanMessage
from src.core.nutrition_advice_agent.common import vision_llm, as_image_part
from src.schemas.meal import DishList


def detect_dishes(image_src: str) -> list[str]:
    """画像から料理名を検出し、重複を除いたリストを返す。

    Args:
        image_src (str): 料理の画像 URL または base64 エンコードされた画像データ

    Returns:
        list[str]: 検出された料理名のリスト

    """
    llm = vision_llm.with_structured_output(DishList)
    msg = HumanMessage(content=[
        {"type": "text", "text": "次の画像に写っている料理名を日本語で列挙し、重複は除いてください。"},
        as_image_part(image_src),
    ])
    response = typing.cast(DishList, llm.invoke([msg]))

    return [d.dish for d in response.dishes]
