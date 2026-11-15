from typing import TypedDict , NotRequired
from langchain_core.messages import AIMessage
from dotenv import load_dotenv, find_dotenv
from langchain_groq import ChatGroq
from langgraph.graph import (StateGraph, START, END, MessagesState)
from IPython.display import Image, display

load_dotenv(find_dotenv())

llm = ChatGroq(
    model="openai/gpt-oss-20b"
)

class State(TypedDict):
    # User input
    question: str
    # Generated answer
    answer: NotRequired[str]
    # Complete model response
    response: NotRequired[AIMessage]
    # Token information
    input_tokens: NotRequired[int]
    output_tokens: NotRequired[int]
    total_tokens: NotRequired[int]

def llm_node(state: State):
        print("\n========================")
        print("LLM NODE")
        print("========================")
    
        response = llm.invoke(state["question"])
        print(
            "\nGenerated Answer:\n",
                response.content
        )
    
        # IMPORTANT:
        # We are NOT counting tokens here.
        # We simply save the complete AIMessage
        # so the next node can inspect its token metadata.
        return { "answer": response.content, "response": response}

def token_counter(state: State):
    print("\n========================")
    print("TOKEN COUNTER NODE")
    print("========================")
    response = state["response"]
    
    usage = response.usage_metadata or {}

    input_tokens = usage.get(
        "input_tokens"
    )

    output_tokens = usage.get(
        "output_tokens"
    )

    total_tokens = usage.get(
        "total_tokens"
    )

    print(
        "Input Tokens:",
        input_tokens
    )

    print(
        "Output Tokens:",
        output_tokens
    )

    print(
        "Total Tokens:",
        total_tokens
    )

    return {"input_tokens": input_tokens, "output_tokens": output_tokens, "total_tokens": total_tokens}

builder = StateGraph(State)

builder.add_node("llm_node",llm_node)
builder.add_node("token_counter", token_counter)

builder.add_edge(START, "llm_node")
builder.add_edge("llm_node", "token_counter")
builder.add_edge("token_counter",END)

graph = builder.compile()

result = graph.invoke({"question": "Tell me about Tata Group in detail."})
print(result)


print(graph.get_graph().draw_mermaid_png())
