from typing import TypedDict
from langgraph.graph import StateGraph, START , END

class State(TypedDict):
    message : str

def first_hello_node(state : State):
    print("message:" f"Hello {state['message']}")

builder = StateGraph(State)
builder.add_node("first_hello_node", first_hello_node)
builder.add_edge(START, "first_hello_node")
builder.add_edge("first_hello_node", END)
mygraph = builder.compile()
mygraph.invoke({"message": "from india"})