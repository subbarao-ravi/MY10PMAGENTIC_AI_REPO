from dotenv import  load_dotenv, find_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableSequence, 
    RunnableParallel, 
    RunnableLambda,
    RunnablePassthrough,
    RunnableBranch
)
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv(find_dotenv())


llm = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash'
)

parser = StrOutputParser()

congratsPrompt = PromptTemplate.from_template(
    "write a short congratulations message for {name} who scored {marks}"
    
)

motivationPrompt = PromptTemplate.from_template(
    "write a short motivational/encouraging message for {name} who scored {marks}"
)

feedbackChain = RunnableBranch(
    (lambda x : x['marks'] >= 50 , congratsPrompt | llm | parser),
    motivationPrompt | llm | parser
)

name = input('enter name ')
marks = int(input('enter marks '))

result = feedbackChain.invoke({"name":name, "marks":marks})
print('Feeb back ', result)