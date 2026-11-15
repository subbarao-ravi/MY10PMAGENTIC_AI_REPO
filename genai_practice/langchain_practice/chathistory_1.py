from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import  load_dotenv, find_dotenv

load_dotenv(find_dotenv())


llm = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash'
)

MESSAGE_SIZE = 3

messages = []
while True:
    user_input = input('enter message ')
    if user_input.lower() == 'exit':
        break

    humanmessage = HumanMessage(content=user_input)
    messages.append(humanmessage)

    recentmessages = messages[-MESSAGE_SIZE:]

    response = llm.invoke(recentmessages)
    print(response.text)
    messages.append(response)


for message in messages:
    print(type(message).__name__,":",message.text)

