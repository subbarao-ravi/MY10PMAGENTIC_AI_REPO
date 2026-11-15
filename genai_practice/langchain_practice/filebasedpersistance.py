from langchain_groq import ChatGroq
from dotenv import load_dotenv,find_dotenv
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import BaseMessage,message_to_dict,messages_from_dict
import json
import os
from pathlib import Path

load_dotenv(find_dotenv())

base_dir = Path(__file__).resolve().parent

class FileChatHistoryMessage(BaseChatMessageHistory):
    def __init__(self, sessionId, storage_path='CHAT_HISTORY'):
        self.sessionId = sessionId
        self.file_path = base_dir / storage_path / f"{sessionId}.json"
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.file_path.exists():
            self.file_path.write_text("[]", encoding='utf=8')
    
    def add_messages(self, messages : list[BaseMessage]) -> None:
        all_messages = list(self.messages)
        all_messages.extend(messages)

        serialized = [message_to_dict(message) for message in all_messages]
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized, file, ensure_ascii=False, indent=2)

    @property
    def messages(self):
        print('filepath',self.file_path.exists())
        if not self.file_path.exists():
            return []
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return messages_from_dict(data)

    def clear(self) -> None: 
        with open(self.file_path, "w", encoding="utf-8" ) as file: 
            json.dump([], file) 




def get_session_history(session_id):
    return FileChatHistoryMessage(session_id)

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




        
        