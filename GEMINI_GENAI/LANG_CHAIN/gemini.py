from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
import main
import logging

logging.getLogger("google_genai").setLevel(logging.ERROR)

model = ChatGoogleGenerativeAI (
    model='gemini-3.8-flash'
)

topic = input('Enter topic name...')
level = input('enter user level..')

templateDict = {"topic": topic, "level": level}

template = PromptTemplate.from_template(
    "Explan {topic} in simple language for a {level}"
)

parser = StrOutputParser()

channel = template | model | parser

response = channel.invoke(templateDict)
print(response)