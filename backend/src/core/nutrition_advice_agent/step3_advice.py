import typing
from src.core.nutrition_advice_agent.common import text_llm
from src.schemas.meal import Advice, BodyInfo


def make_advice(nutrients: list[dict], body: BodyInfo) -> str:
    """個人情報と栄養素一覧を基に、健康アドバイスを生成する。
    Args:
        nutrients (list[dict]): 各料理の栄養素リスト
        body (BodyInfo): ユーザーの身体情報
    Returns:
        str: 生成された健康アドバイス
    """
    llm = text_llm.with_structured_output(Advice)
    user_prompt = (
        "以下の個人情報と今日食べた料理の栄養素一覧を踏まえて、"
        "具体的な健康アドバイスを 300 字以内で日本語でください。"
    )
    content = f"{user_prompt}\n\n▼個人情報\n{body.json()}\n\n▼栄養素一覧\n{nutrients}"

    response = typing.cast(Advice, llm.invoke(content))

    return response.advice
