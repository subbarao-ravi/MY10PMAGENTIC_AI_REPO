from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv , find_dotenv

load_dotenv(find_dotenv())

print('-------------Runnable Lambda--------------')

values = {}

def add_ten(x):
    result=x+10
    values['add_ten'] = result
    return result

def multiply_ten(x):
     result= x*10
     values['multiply_ten'] = result
     return result

def sub_ten(x):
     result=x-10
     values['sub_ten'] = result
     return result

add = RunnableLambda(add_ten)
mul = RunnableLambda(multiply_ten)
sub = RunnableLambda(sub_ten)


chain = add | mul | sub
result = chain.invoke(10)
print(result)
print(values)

print('---------common save method-----------')

def save(name, value):
     values[name] = value
     return value

add_1 = RunnableLambda(
     lambda x : save('add_save_ten',x+10)
)

mul_1 = RunnableLambda(
     lambda x: save('mul_save_ten',x*10)
)

sub_1 = RunnableLambda(
     lambda x : save('sub_save_ten', x-10)
)

chain_1 = add_1 | sub_1 | mul_1

result = chain_1.invoke(10)
print(result)
print(values)
