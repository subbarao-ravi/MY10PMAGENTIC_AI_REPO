from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv , find_dotenv
from langchain_openai import ChatOpenAI


load_dotenv(find_dotenv())

print('-------------Runnable Lambda--------------')

llm = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash'
)

# llm = ChatOpenAI(
#     model='gpt-4.1-mini'
# )

parser = StrOutputParser()

prompt = PromptTemplate.from_template(
    '''
    Explain {topic} in simple english
    proivde simple definition
    provide 5 important points
    '''
)

inputs =[
    {"topic": "Python"}, 
    {"topic": "Java"}, 
    {"topic": "SQL"}
]

prompt2 = PromptTemplate.from_template(
    '''
        From the above explantions provide top 5 interview questions from each topic
        while giving the interview questions mention interview question with corresponding topic

        Explanation :
        {explanation}
    '''
)

topicwise_explanation = RunnableLambda(
    lambda explanation : {"explanation": explanation}
)

chain = prompt | llm | parser | topicwise_explanation | prompt2 | llm | parser
results = chain.batch(inputs)

for result in results:
    print(result)

print('--------------chain steps-----------')
print(chain.steps)
 