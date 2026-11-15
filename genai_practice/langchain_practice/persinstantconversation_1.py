from langchain_groq import ChatGroq
from dotenv import load_dotenv,find_dotenv
from langchain_core.messages import (SystemMessage,
                                     HumanMessage,
                                     message_to_dict,
                                     messages_from_dict,
                                     convert_to_messages
                            )
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
import json

load_dotenv(find_dotenv())

messages = [
         (
             "system", "You are helpful assistant"
         ),
         (
             "human", "i am subbarao"
         )
    ]

messageList = convert_to_messages(messages)
serialized = [message_to_dict(m) for m in messageList]
print(serialized)

json_string = json.dumps(
                serialized,
                indent=2
            )

print(json_string)

pythonData = json.loads(json_string)
print(pythonData)

messagesDict = messages_from_dict(pythonData)
print(messagesDict)

