from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)
modelopenai=ChatOpenAI()
#ollama gemma
gemmallm=Ollama(model="Llama2")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 50 words")
prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 50 words")

add_routes(
    app,
    prompt1|modelopenai,
    path="/essay"


)

add_routes(
    app,
    prompt2|gemmallm,
    path="/poem"


)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)