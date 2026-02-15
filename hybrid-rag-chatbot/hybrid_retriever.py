from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from graph_store import graph_search

embeddings = OpenAIEmbeddings()

vectordb = Chroma(
    persist_directory="vector_db",
    embedding_function=embeddings
)

def hybrid_search(user_query):

    print("\n============================")
    print("USER QUERY:", user_query)

    # VECTOR SEARCH
    print("\n=== VECTOR SEARCH ===")

    vector_results = vectordb.similarity_search(
        user_query,
        k=2
    )

    for i, doc in enumerate(vector_results):
        print(f"\nVector Result {i+1}:")
        print(doc.page_content)

    # GRAPH SEARCH

    graph_query = """
    MATCH (p:Person)-[r]->(n)
    RETURN p.name, type(r), n.name
    """

    graph_results = graph_search(graph_query)

    return vector_results, graph_results
