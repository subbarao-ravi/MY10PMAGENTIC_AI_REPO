from langchain_classic.memory import (ConversationBufferMemory,
                                      ConversationBufferWindowMemory)
from langchain_classic.chains.conversation.base import ConversationChain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

llm = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash"
)

memory = ConversationBufferWindowMemory(
    k=2
)

conversation = ConversationChain(
    llm= llm,
    memory=memory
)

result = conversation.invoke(
    {
        "input" : "my secret code is 255"
    }
)
print('first resp ',result['response'])

result = conversation.invoke(
    {
        "input" : "i am learning python"
    }
)
print('2nd resp ',result['response'])

result = conversation.invoke(
    {
        "input" : "i lives in hyderabad"
    }
)
print('3rd resp ',result['response'])

result = conversation.invoke(
    {
        "input" : "what is my secret code"
    }
)
print('4th resp ',result['response'])