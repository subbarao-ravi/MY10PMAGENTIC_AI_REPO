from dotenv import load_dotenv,find_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel, Field, ValidationError

load_dotenv(find_dotenv())

llm = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash'
)

parser = StrOutputParser()

class Student(BaseModel):
    name :str = Field(description='name of the student')
    age : int = Field(description='age of the student')
    #course : str | None = 'LangChain'
    skills : list[str] = Field(
        #default=['JAVA','PYTHON'], 
        default_factory= lambda :['JAVA','PYTHON'],
        description='skills of the student')

#s1 = Student(name='SHIVA',age='20', course='ALLRounder')
# print(s,s1)
# print(s.model_dump())
# print(s.model_dump_json())

# print(s1.model_dump())
# print(s1.model_dump_json())

# s_llm = llm.with_structured_output(Student)
# resp = s_llm.invoke('RAMA IS GOOD BOY WITH 16 YEARS OF AGE')
# print(resp)


class Product(BaseModel):
    name : str = Field(description='Name of the product')
    qty : float = Field(default=1.0, description='Quantity of the product')
    category : str = Field(description='Category of the product')
    in_stock : bool = Field(default=False, description='Is product available in the stock or not')


#p = Product(name = "Iphone18",category = "smartphone",price = 300000,in_stock=True)
# print(p) 
# print(p.name) 
# print(p.model_dump()) #dict 
# print(type(p.model_dump())) #dict 
# print(p.model_dump_json()) #json 
# print(type(p.model_dump_json())) #json

pllm = llm.with_structured_output(Product, include_raw=True)
result = pllm.invoke('iphone18 with smartphone category having 1000 price not available in stock')
print(result)
print(result['parsed'])
print(result['parsing_error'])


