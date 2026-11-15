from dotenv import load_dotenv,find_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv(find_dotenv())

llm = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash'
)

parser = StrOutputParser()

cpt = ChatPromptTemplate.from_messages([      
    SystemMessage('you are helpful programming language allrounder'),
    HumanMessage('explain python language in simple way for beginner')                              
])

prompt = cpt.invoke({})
print(type(prompt))
for message in prompt.messages:
    print(type(message).__name__,":",message.content)


cpt1 = ChatPromptTemplate.from_messages([      
    ('system','you are helpful programming language allrounder'),
    ('human','explain python language in simple way for beginner')                              
])

print(cpt1)

print()
prompt = cpt1.invoke({})
response = llm.invoke(prompt)
output = parser.invoke(response)
print(output)