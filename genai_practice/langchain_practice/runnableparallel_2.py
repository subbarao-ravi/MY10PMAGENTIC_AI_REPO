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

blogPrompt = PromptTemplate.from_template(
    '''
    Create a blog on {topic}
    provide 5 important blog points for post
    use simple english
    '''
)

blogChain = blogPrompt | llm | parser

social_Prompt = PromptTemplate.from_template(
    '''
        Create a social media post about {topic}
        which should be more interactive and attractive
        keep it in simple english
    '''
)

socialChain = social_Prompt | llm | parser

summary_Prompt = PromptTemplate.from_template(
    '''
        Create a short summary for readers about {topic}
        keep it simple and understandable
    '''
)

summaryChain = summary_Prompt | llm | parser

parallel = RunnableParallel(
    query = RunnablePassthrough(),
    blogBranch = blogChain,
    socialBranch = socialChain,
    summaryBranch = summaryChain
)

result = parallel.invoke({"topic": "Artificial Intelligence"})
print('query', result['query'])
print('blogBranch', result['blogBranch'])
print('socialBranch', result['socialBranch'])
print('summaryBranch', result['summaryBranch'])