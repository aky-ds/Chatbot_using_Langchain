import os 
import langchain
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
from fastapi import FastAPI
import uvicorn

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

parser=StrOutputParser()

chain=prompt | llm | parser

app=FastAPI(
    title='My Content Writer',
    description='End to End COntent writer'
)

add_routes(app,chain)

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)
