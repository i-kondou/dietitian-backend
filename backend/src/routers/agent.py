from dotenv import load_dotenv
from fastapi import APIRouter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
import os

import src.schemas.agent as agent_schema

router = APIRouter()

@router.get("/users/me", response_model=agent_schema.AgentResponse)
async def generate_agent_response(agent_request_body: agent_schema.AgentRequest):
    """
    エージェントに料理画像のURLを渡し、それに関してカロリーや栄養素、アドバイスを返します。
    """
    load_dotenv()

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-preview-04-17", temperature=0)
    prompt = ChatPromptTemplate(
        [
            ("system", "あなたは優秀な栄養士です。"),
            ("human", "{input}"),
        ]
    )
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    # return agent_schema.AgentResponse(content=chain.invoke({"input", agent_request_body.}))