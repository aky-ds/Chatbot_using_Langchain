import os 
import langchain
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.output_parsers import StrOutputParser
# loading the keys

load_dotenv()

os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['GOOGLE_API_KEY']=os.getenv('GOOGLE_API_KEY')

# Loading the model

llm=GoogleGenerativeAI(model='gemini-pro',temperature=0.1)

# Create a Template

prompt=ChatPromptTemplate.from_messages([
    ('system','You are an excellent content writer so write on a topic given by the user'),
    ('user','{user_query}')
])
st.title('AI Content Writer')
# Create an Application
user_query=st.text_input('Enter the name of the topic')


if st.button('Generate'):
    response=llm.invoke(user_query)
    st.write(response)