from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    message : str

def function01(state: State):
    print("function01 invoked")
    return {"text": f"Hello {state['message']}!"}

def function02(state: State):
    print("function02 invoked")
    return {"text": f"Hello {state['message']}!"}

builder = StateGraph(State)

builder.add_node("function01", function01)
builder.add_node("function02", function02)

builder.add_edge(START, "function01")
builder.add_edge("function01", "function02")
builder.add_edge("function02", END)

mygraph = builder.compile()
response = mygraph.invoke({"message": "from india"})
print(response)