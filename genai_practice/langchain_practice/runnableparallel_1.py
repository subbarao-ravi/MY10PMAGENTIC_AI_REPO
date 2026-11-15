from dotenv import  load_dotenv, find_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableSequence, 
    RunnableParallel, 
    RunnableLambda,
    RunnablePassthrough
)
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv(find_dotenv())

llm = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash'
)

parser = StrOutputParser()

jokePrompt = PromptTemplate.from_template(
    '''
    Tell me a famous joke about {topic}
    when providing the joke mention The topic name and then joke 
    '''
)

jokeChain = jokePrompt | llm | parser

motivationalPrompt = PromptTemplate.from_template(
    '''
    Tell me a famous motiviational speech from {topic}
    '''
)

motiChain = motivationalPrompt | llm | parser

parallelPipe = RunnableParallel(
    jokeBranch = jokeChain,
    motivationBranch = motiChain
)

result = parallelPipe.invoke({"topic":"elon musk"})
print('jokeBranch', result['jokeBranch'])
print('motivationBranch', result['motivationBranch'])
