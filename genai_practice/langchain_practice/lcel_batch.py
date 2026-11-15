from dotenv import load_dotenv,find_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import time

load_dotenv(find_dotenv())

llm = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash'
)

parser = StrOutputParser()

prompt = PromptTemplate.from_template('explain {topic} in simple way')

chain = prompt | llm | parser

inputs = [
    {"topic":"java"},
    {"topic":"python"},
    {"topic":"devops"},
    {"topic":"langchain"}
]

results = chain.batch(inputs)
for result in results:
    print(result)
    time.sleep(10)
