from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

# FastAPIのインスタンスを作成
app = FastAPI()

# --- Pydanticモデルの定義 ---
# POSTリクエストで受け取るデータの型を定義


class Item(BaseModel):
    """
    Itemモデルは、POSTリクエストで受け取るデータの型を定義します。
    - name: アイテムの名前
    - price: アイテムの価格
    - description: アイテムの説明（オプション）
    - tax: アイテムの税金（オプション）
    """
    name: str
    price: float
    description: Union[str, None] = None
    tax: Union[float, None] = None


# --- APIエンドポイントの定義 ---

@app.get("/")
def read_root() -> dict:
    """
    ルートエンドポイント。サーバーが起動しているかを確認できます。
    """
    return {"message": "Hello, FastAPI World!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None) -> dict:
    """
    パスパラメータ(item_id)と、オプショナルなクエリパラメータ(q)を受け取ります。
    例: /items/5?q=somequery
    """
    return {"item_id": item_id, "q": q}


@app.post("/items/")
def create_item(item: Item) -> Item:
    """
    リクエストボディとしてItemデータを受け取り、それをそのまま返します。
    データのバリデーションはPydanticモデルによって自動的に行われます。
    """
    return item
