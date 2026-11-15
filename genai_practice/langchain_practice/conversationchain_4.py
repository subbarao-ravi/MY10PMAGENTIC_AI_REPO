from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash"
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

humanmessage = [
    HumanMessage(content="my name is subbarao")
]

response = chatbot.invoke(
    humanmessage,
    config={
        "configurable":{
            "session_id":"subbarao"
        }
    }
)

print('response ',response.content)

humanmessage2 = [
    HumanMessage(content="what is my name")
]

response2 = chatbot.invoke(
    humanmessage2,
    config={
        "configurable":{
            "session_id":"ravi"
        }
    }
)

print('response2',response2.content)

