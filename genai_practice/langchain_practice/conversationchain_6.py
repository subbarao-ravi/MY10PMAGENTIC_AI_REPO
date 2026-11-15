from langchain_groq import ChatGroq
from dotenv import load_dotenv,find_dotenv
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv(find_dotenv())

llm = ChatGroq(
    model="openai/gpt-oss-120b"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are an helpful assistant"),
        ("human","{question}"),
        MessagesPlaceholder(
            variable_name="history"
        )
    ]
)

chain = prompt | llm

store = {}
def get_session_history(sessionId):
    if sessionId not in store:
        store[sessionId]= (
            InMemoryChatMessageHistory()
        )

    return store[sessionId]


chat = RunnableWithMessageHistory(
    chain,
    get_session_history,
    history_messages_key="history",
    input_messages_key="question"
)

sessionId = input('enter sessionId for chatting: ')
while True:
    user_input = input("You ")
    if user_input.lower() == 'exit':
        break

    response = chat.invoke(
        {
            "question":user_input
        },
        config={
            "configurable":{
                "session_id":sessionId
            }
        }
    )
    print(response.content)
    print('=================')