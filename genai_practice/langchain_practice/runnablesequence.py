from dotenv import load_dotenv,find_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv(find_dotenv())

llm = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash'
)

parser = StrOutputParser()

prompt = PromptTemplate.from_template('explain python in simple way and provide short description')

chain = RunnableSequence(prompt, llm, parser)

result = chain.invoke({})

print(result)