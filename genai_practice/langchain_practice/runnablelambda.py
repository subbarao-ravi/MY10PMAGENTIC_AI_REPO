from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv , find_dotenv

load_dotenv(find_dotenv())

add_ten = RunnableLambda(
    lambda x : x+10
)
multiply_ten = RunnableLambda(
    lambda x: x * 10
)
sub_two = RunnableLambda(
    lambda x: x-2
)
chain = add_ten | multiply_ten | sub_two
result = chain.invoke(10)
print(result)
print(chain.steps)

print('-------------Runnable Lambda--------------')

llm = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash'
)

parser = StrOutputParser()

prompt1 = PromptTemplate.from_template(
    ''' explain {topic} in simple way for beginners
        Give simple definition
        provide 5 important points
    '''
)

prompt2 = PromptTemplate.from_template(
    '''
        Based on the below explanation 
        create 5 beginner interview questions
        while giving the interview questions mention interview questions

        explanation :
        {explanation}
    '''
)

explanation_dict = RunnableLambda(
    lambda explanation : {"explanation":explanation}
)

chain = prompt1 | llm | parser | explanation_dict | prompt2 | llm | parser

topic = input('enter topic ')

response = chain.invoke({"topic" : topic})

print('response ',response)