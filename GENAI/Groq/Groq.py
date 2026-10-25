import os
from click import prompt
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
#os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")
st.title("Chat with Groq")

temperature = st.slider("Temperature", 0.0, 1.0, 0.7)

#prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are helpful Assistant"),
         ("user","Question: {question}")
    ]
)

##llm model initialization
llm = ChatGroq(
      model = "openai/gpt-oss-120b",
      temperature = temperature
)


#controlling output format
output = StrOutputParser()

chain = prompt|llm|output

input_text = st.text_input("Ask your questions")

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)