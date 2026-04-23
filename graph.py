from typing import TypedDict
from langgraph.graph import StateGraph, END
from retriever import retriever
from grok_llm import ask_llm

class State(TypedDict):
    query: str
    context: str
    answer: str

# Process Node
def process_node(state):
    query = state["query"]

    # Search relevant chunks
    docs = retriever.invoke(query)

    # If no result
    if not docs:
        state["answer"] = "No relevant data found. Escalated to Human Support."
        return state

    # Combine context
    context = "\n".join([doc.page_content for doc in docs])
    state["context"] = context

    # HITL conditions
    lower_query = query.lower()

    if "fraud" in lower_query or "angry" in lower_query or "legal" in lower_query:
        state["answer"] = "Your issue has been escalated to Human Support Team."
        return state

    # Prompt for LLM
    prompt = f"""
Use the below customer support knowledge base context.

Context:
{context}

Question:
{query}

Give clear professional answer.
"""

    response = ask_llm(prompt)

    state["answer"] = response
    return state

# Output Node
def output_node(state):
    print("\nBOT RESPONSE:\n")
    print(state["answer"])
    return state

# Build Graph
builder = StateGraph(State)

builder.add_node("process", process_node)
builder.add_node("output", output_node)

builder.set_entry_point("process")

builder.add_edge("process", "output")
builder.add_edge("output", END)

graph = builder.compile()