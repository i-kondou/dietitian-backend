import base64
from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

vision_llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
text_llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


def image_to_base64(image_path: str) -> str:
    """base64エンコードされた画像データを返す。

    Args:
        image_path (str): 画像ファイルのパス

    Returns:
        str: base64エンコードされた画像データ

    """
    return base64.b64encode(Path(image_path).read_bytes()).decode("utf-8")


def as_image_part(src: str) -> dict:
    """ChatGoogleGenerativeAIのメッセージ形式に変換する。

    Args:
        src (str): 画像のURLまたはbase64エンコードされた画像データ

    Returns:
        dict: ChatGoogleGenerativeAIのメッセージ形式

    """
    if src.startswith("http://") or src.startswith("https://"):
        return {
            "type": "image_url",
            "image_url": {"url": src}
        }
    return {"type": "image_url", "image_url": f"data:image/jpeg;base64,{image_to_base64(src)}"}
