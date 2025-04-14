#!/usr/bin/env python
from typing import List

from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes
from dotenv import load_dotenv
load_dotenv()

# Codza "1. Adım: Prompt şablonunu oluştur"
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# Codza "2. Adım: Modeli oluştur"
model = ChatOpenAI()

# Codza "3. Adım: Çıktı ayrıştırıcısını oluştur"
parser = StrOutputParser()

# Codza "4. Adım: Zinciri oluştur"
chain = prompt_template | model | parser


# Codza "5. Adım: Uygulama tanımı"
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# Codza "6. Adım: Zincir rotasını ekle"

add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
