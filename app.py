from graph import graph

print("RAG Customer Support Assistant Started")
print("Type 'exit' to quit\n")

while True:
    query = input("Ask Your Question: ")

    if query.lower() == "exit":
        print("Chatbot Closed.")
        break

    graph.invoke({
        "query": query,
        "context": "",
        "answer": ""
    })