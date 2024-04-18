import requests
import streamlit as st

#function to get response from openai
def get_openai_response(input_text):
    response=requests.post("http://localhost:8000/essay/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']['content']

#function to get response from ollama
def get_ollama_response(input_text):
    response=requests.post("http://localhost:8000/poem/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']

#streamlit interface

st.title('AI content with OPENAI and LLAMA2 API')
input_text=st.text_input("AI content with openai")
input_text_ollama=st.text_input("AI content with ollama")

if input_text:
    openai_responce=(get_openai_response(input_text))
    st.write(openai_responce)

if input_text_ollama:
    ollama_responce=(get_ollama_response(input_text1))
    st.write(ollama_responce)