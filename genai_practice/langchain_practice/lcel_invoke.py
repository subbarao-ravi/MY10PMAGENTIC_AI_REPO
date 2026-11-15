from dotenv import load_dotenv,find_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv(find_dotenv())

llm = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash'
)

parser = StrOutputParser()

prompt = PromptTemplate.from_template(
    '''
        Explain {topic} in simple {language}
        for {level}

        Give {sample} examples which are familiar

        Provide top {questions} interview questions with clear explanation
    '''
    )

topic = input('enter topic ')
language = input('enter language ')
level = input('enter level ')
sample = int(input('provide number of examples '))
questions = int(input('enter number of interview questions '))

promptDict = {"topic":topic,
              "language" : language, 
              "level":level, 
              "sample":sample,
              "questions":questions
              }

chain = prompt | llm | parser

result = chain.invoke(promptDict)

print(result)