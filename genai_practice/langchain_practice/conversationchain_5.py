from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from dotenv import load_dotenv,find_dotenv

from langchain_groq import ChatGroq

load_dotenv(find_dotenv())

llm = ChatGroq(
    #model="gemini-3.5-flash"
    model="openai/gpt-oss-120b"
)

store = {}

def get_session_history(sessionId):
    if sessionId not in store:
        store[sessionId] = (
            InMemoryChatMessageHistory()
        )

    return store[sessionId]


chatbot = RunnableWithMessageHistory(
    llm,
    get_session_history
)

print('INTERACTIVE CHAT BOT')
print('----------------------')
print()
sessionId = input('enter sessionId to store information ')
print()
while True:
    user_input = input('You ')
    if user_input.lower() == 'exit':
        break

    humanMsg = [HumanMessage(
        content=user_input
    )]

    response =  chatbot.invoke(
        humanMsg,
        config={
            "configurable":{
                "session_id": sessionId
            }
        }
    )

    print('type of resp ',type(response))
    print('response ',response.content)
