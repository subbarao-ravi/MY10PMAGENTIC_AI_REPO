from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import  load_dotenv, find_dotenv
from langchain_core.messages import HumanMessage,SystemMessage

load_dotenv(find_dotenv())


llm = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash'
)

messages = []
while True:
    user_input = input('enter message ')
    if user_input.lower() == 'exit':
        break

    humanmessage = HumanMessage(content=user_input)
    messages.append(humanmessage)

    response = llm.invoke(messages)
    print(response.text)
    messages.append(response)


for message in messages:
    print(type(message).__name__)
    print(message.text)

