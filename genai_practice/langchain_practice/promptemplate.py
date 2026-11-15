from dotenv import load_dotenv,find_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_core.prompts import PromptTemplate

load_dotenv(find_dotenv())

llm = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash'
)
topic = input('enter topic name: ')
level = input('enter level: ')
pt = PromptTemplate.from_template('explain {topic} at {level}',partial_variables={"topic" : topic, "level":level})
tempResp = pt.invoke({"topic":"java"})
print('tempResp ',tempResp)

#response = llm.invoke(tempResp)
#print(response.text)