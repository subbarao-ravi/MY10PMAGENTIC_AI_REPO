from dotenv import load_dotenv, find_dotenv
import os
from langchain_openai import ChatOpenAI

load_dotenv(find_dotenv(), override=True)
#load_dotenv(r"C:\MY10PMAGENTIC_AI\.env", override=True)

model = ChatOpenAI(
    model='gpt-4o-mini',
    api_key=os.getenv('OPENAI_API_KEY')
)

response = model.invoke('Explain AI in simple language for a beginner')
print(response.content)