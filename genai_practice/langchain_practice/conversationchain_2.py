from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from dotenv import load_dotenv, find_dotenv
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains.conversation.base import ConversationChain

load_dotenv(find_dotenv())

llm = ChatOllama(
    model="llama3.1"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        MessagesPlaceholder("history")
    ]
)

history = [
    ("human","my name is subbarao"),
    ("ai","hello subbarao")
]

result = prompt.invoke({
    "history":history
})

print('result ',result)