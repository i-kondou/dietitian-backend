import typing
from src.core.nutrition_advice_agent.common import text_llm
from src.schemas.meal import Advice, BodyInfo

PROMPT = """
# 命令
あなたは経験豊富な管理栄養士です。以下の入力情報を基に、ユーザーの次の食事がより良くなるような、実践的で具体的なアドバイスを生成してください。

# あなたの役割
* プロの管理栄養士として、専門的な知識に基づきつつも、親しみやすく、ユーザーのやる気を引き出すようなアドバイスをします。
* 単に栄養素の過不足を指摘するだけでなく、それを解決するための「具体的な料理」や「食材の組み合わせ」を提案することが最も重要です。

# 入力情報
* **個人情報**:
    * [ユーザーの年齢、性別、身体活動レベルなどを記載]
* **今日食べた料理の栄養素一覧**:
    * [LLMに渡す栄養素データを記載]

# 出力形式とルール
* まず、現在の食事の良い点を1つ具体的に褒めてください。
* 次に、最も改善すべき栄養バランスの課題を1つ指摘してください。
* その課題を解決するために、**次回の食事で追加・変更すべき具体的な料理名や食材を2つ提案**してください。
* 例：「夕食にわかめと豆腐の味噌汁を追加しませんか？」
* 例：「パンを全粒粉パンに変えてみましょう」
* アドバイスの全体を、親しみやすい日本語で300字以内でまとめてください。

"""


def make_advice(nutrients: list[dict], body: BodyInfo) -> str:
    """個人情報と栄養素一覧を基に、健康アドバイスを生成する。
    Args:
        nutrients(list[dict]): 各料理の栄養素リスト
        body(BodyInfo): ユーザーの身体情報
    Returns:
        str: 生成された健康アドバイス
    """
    llm = text_llm.with_structured_output(Advice)
    user_prompt = PROMPT
    content = f"{user_prompt}\n\n▼個人情報\n{body.json()}\n\n▼栄養素一覧\n{nutrients}"

    response = typing.cast(Advice, llm.invoke(content))

    return response.advice
