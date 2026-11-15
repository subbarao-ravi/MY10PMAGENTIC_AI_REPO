from typing import TypedDict
from langgraph.graph import (StateGraph, START, END, MessagesState)
from dotenv import load_dotenv, find_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv(find_dotenv())

llm = ChatGroq(
    model="openai/gpt-oss-20b"
)

def call_model(state : MessagesState):
    print("\n=========================")
    print("MYBOT NODE")
    print("=========================")

    print(state)
    messages = state['messages']

    print(
        "Current Messages:",
        messages
    )

    response = llm.invoke(messages)
    print("model response ",response.content)

    # MessagesState internally uses add_messages reducer.
    # Therefore the new AIMessage will be added
    # to the existing list of messages.
    return {
        "messages": [response]
    }


workflow = StateGraph(MessagesState)

workflow.add_node("call_model", call_model)

workflow.add_edge(START, "call_model")
workflow.add_edge("call_model" , END)

mygraph = workflow.compile()

input_messages = {
    "messages":[
        HumanMessage(content="tell about tesla")
    ]
}

graphresponse = mygraph.invoke(input_messages)
print("graphresponse ",graphresponse)
