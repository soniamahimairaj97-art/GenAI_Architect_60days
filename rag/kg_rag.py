import os
import sys
from dotenv import load_dotenv
from neo4j import GraphDatabase
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# ── Path & env setup ──────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "utils"))
load_dotenv(os.path.join(BASE_DIR, ".env"), override=True)

KG_SYSTEM_PROMPT = """
You are a medical knowledge expert. Use the provided knowledge graph
context to explain relationships between medical entities (conditions,
medications, symptoms, lab values) found in the report.
"""


class KGRag:
    def __init__(self):
        uri      = os.getenv("NEO4J_URI",      "bolt://localhost:7687")
        username = os.getenv("NEO4J_USERNAME",  "neo4j")
        password = os.getenv("NEO4J_PASSWORD",  "")
        api_key  = os.getenv("OPENAI_API_KEY",  "").strip()

        self.driver = GraphDatabase.driver(uri, auth=(username, password))
        self.llm    = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.2,
            api_key=api_key
        )
        print("[KGRag] Connected to Neo4j.")

    def ingest_chunks(self, chunks: list, doc_id: str):
        """Store document chunks as nodes in Neo4j."""
        with self.driver.session() as session:
            session.run(
                "MATCH (n:Chunk {doc_id: $doc_id}) DETACH DELETE n",
                doc_id=doc_id
            )
            for i, chunk in enumerate(chunks):
                session.run(
                    "CREATE (:Chunk {id: $id, doc_id: $doc_id, "
                    "text: $text, index: $index})",
                    id=f"{doc_id}_{i}",
                    doc_id=doc_id,
                    text=chunk,
                    index=i
                )
            session.run("""
                MATCH (a:Chunk {doc_id: $doc_id}),
                      (b:Chunk {doc_id: $doc_id})
                WHERE b.index = a.index + 1
                CREATE (a)-[:NEXT]->(b)
            """, doc_id=doc_id)
        print(f"[KGRag] Ingested {len(chunks)} chunks into Neo4j.")

    def query(self, question: str, doc_id: str) -> str:
        """Retrieve relevant chunks from KG using keyword matching."""
        keywords = question.lower().split()[:5]
        seen     = set()
        unique   = []

        with self.driver.session() as session:
            for kw in keywords:
                results = session.run(
                    "MATCH (c:Chunk {doc_id: $doc_id}) "
                    "WHERE toLower(c.text) CONTAINS $kw "
                    "RETURN c.text LIMIT 3",
                    doc_id=doc_id,
                    kw=kw
                )
                for r in results:
                    text = r["c.text"]
                    if text not in seen:
                        seen.add(text)
                        unique.append(text)

        context = "\n\n".join(unique) if unique else "No relevant data found."

        messages = [
            SystemMessage(content=KG_SYSTEM_PROMPT),
            HumanMessage(
                content=f"Knowledge Graph Context:\n{context}"
                        f"\n\nQuestion: {question}"
            )
        ]
        response = self.llm.invoke(messages)

        if hasattr(response, "content"):
            return str(response.content)
        return str(response)

    def close(self):
        self.driver.close()
        print("[KGRag] Neo4j connection closed.")