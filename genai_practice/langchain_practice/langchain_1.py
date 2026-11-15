from dotenv import load_dotenv,find_dotenv
from pathlib import Path
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage

load_dotenv(find_dotenv(), override=True)

llm = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash'
)

msgs = []
sysmsg = SystemMessage(content= 'You are an experienced python teacher')
msgs.append(sysmsg)

while True:
    humanmsg = input("User:")
    if humanmsg.lower() == 'exit':
        break

    msgs.append(HumanMessage(content=humanmsg))
    response = llm.invoke(msgs)
    msgs.append(response)
    print(response.text)




