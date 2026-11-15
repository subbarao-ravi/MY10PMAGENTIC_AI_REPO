from langchain_classic.memory import (ConversationBufferMemory,
                                      ConversationBufferWindowMemory)
from langchain_google_genai import ChatGoogleGenerativeAI

# from dotenv import  load_dotenv, find_dotenv

# load_dotenv(find_dotenv())

# llm = ChatGoogleGenerativeAI(
#     model='gemini-3.5-flash'
# )


memory = ConversationBufferWindowMemory(
    k=1,
    return_messages= True
)

memory.save_context(
    {
        "input":"my name is subbarao",
    },
    {
    "output":"nice to meet you how can i assist you"
    }
)

memory.save_context(
    {
        "input":"I am learning python",
    },
    {
    "output":"that't great"
    }
)

result = memory.load_memory_variables({})
for message in result['history']:
    print(type(message).__name__,":",message.content)