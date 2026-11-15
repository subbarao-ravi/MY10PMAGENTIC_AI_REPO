from langchain_classic.memory import (ConversationBufferMemory,
                                      ConversationBufferWindowMemory)

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_classic.chains.conversation.base import ConversationChain

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

llm = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash'
)

memory = ConversationBufferMemory()

chain = ConversationChain(
    llm= llm,
    memory=memory
)

result = chain.invoke(
    {
    "input":"my name is subbarao"
    }
)

print(result['response'])

print('---------------------------')

result = chain.invoke(
    {
        "input":"what is my name"
    }
)
print(result['response'])