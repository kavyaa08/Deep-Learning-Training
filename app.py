from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts  import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Creating my prompts
prompt = ChatPromptTemplate.from_messages(
    [
        ("system" ,"You are a helpful AI bot. please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

# streamlit framework 
st.title('langchain demo with gemma: 2b')
input_text = st.text_input('what question do you have in ')

#Ollama Model
llm = Ollama(model="gemma2:2b")
output_parser=StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
