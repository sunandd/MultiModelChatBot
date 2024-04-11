from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a inteligent assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

# streamlit framework

st.title('Langchain With Local Gemma Chatbot')
input_text=st.text_input("Search the topic as you want")

# ollama Gemma LLm 
llm=ollama(model="gemma")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
