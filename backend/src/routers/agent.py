import base64
from dotenv import load_dotenv
from fastapi import APIRouter, File, HTTPException, UploadFile, Form
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Annotated

import src.schemas.agent as agent_schema
from src.core.enums import Sex

router = APIRouter()

@router.post("/users/me/agent", response_model=agent_schema.AgentResponse)
async def generate_agent_response(height: Annotated[float, Form(description="身長(cm)")], weight: Annotated[float, Form(description="体重(kg)")], age: Annotated[int, Form(description="年齢")], sex: Annotated[Sex, Form(description="性別")], image: UploadFile = File(..., description="料理画像")):
    """
    エージェントに料理画像を渡し、それに関してカロリーや栄養素、アドバイスを返します。
    """
    load_dotenv()

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-preview-04-17", temperature=0)
    if not llm:
        raise HTTPException(status_code=500, detail="サーバー側でGeminiモデルが初期化されていません。")

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "あなたは、優秀な栄養士です。提供された画像から料理を分析し、専門的な知見に基づいて回答してください。"),
            (
                "human", 
                [
                    { "type": "text", "text": "画像の料理について、カロリーと栄養素を教えてください。"},
                    { "type": "image_url", "image_url": "{image_data_uri}"}
                ]
            )
        ]
    )

    output_parser = StrOutputParser()

    chain = (RunnablePassthrough.assign(
        image_data_uri=lambda inputs: f"data:{inputs['mime_type']};base64,{base64.b64encode(inputs['image_bytes']).decode('utf-8')}"
    )) | prompt | llm | output_parser

    image_contents = await image.read()
    base64_image = base64.b64encode(image_contents).decode("utf-8") # 画像をBase64に(Geminiに入力できる形式)

    mime_type = image.content_type
    if not mime_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="アップロードされたファイルが画像ではありません。")

    try:
        response = await chain.ainvoke({
            "mime_type": mime_type,
            "image_bytes": image_contents,
        })
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"チェーンの実行中にエラーが発生しました。{str(ex)}")

    return agent_schema.AgentResponse(content=response)