from hybrid_retriever import hybrid_search
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

print("\n=== HYBRID RAG CHATBOT STARTED ===")

while True:

    user_query = input("\nYou: ")

    if user_query.lower() == "exit":
        break

    vector_results, graph_results = hybrid_search(user_query)

    context = ""

    for doc in vector_results:
        context += doc.page_content + "\n"

    context += graph_results

    print("\n=== FINAL CONTEXT SENT TO LLM ===")
    print(context)

    prompt = f"""
    Answer using this context:

    {context}

    Question: {user_query}
    """

    response = llm.invoke(prompt)

    print("\nChatbot:", response.content)
