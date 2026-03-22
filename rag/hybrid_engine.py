import os
import sys
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# ── Path & env setup ──────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "rag"))
sys.path.insert(0, os.path.join(BASE_DIR, "utils"))
load_dotenv(os.path.join(BASE_DIR, ".env"), override=True)

from traditional_rag import TraditionalRAG   # noqa: E402
from kg_rag import KGRag                     # noqa: E402

SIMILARITY_THRESHOLD = 0.30   # raise to 0.70 once hybrid mode confirmed working

COMBINE_PROMPT = """
You have two answers about a medical report. Combine them into one clear,
simple explanation for the patient.

Answer from vector search:
{vector_answer}

Answer from knowledge graph:
{kg_answer}

Provide a single unified, patient-friendly explanation. Be warm and simple.
"""

MEDICAL_SYSTEM_PROMPT = """
You are a compassionate medical assistant that explains medical reports
to patients in simple, non-technical language.

Rules:
- Use plain English. Avoid jargon.
- Explain what the findings mean for the patient.
- Highlight any urgent items in simple terms.
- Never diagnose. Always suggest consulting a doctor.
- Be warm, reassuring, and clear.
"""


class HybridRAGEngine:
    def __init__(self):
        print("[HybridRAGEngine] Initializing...")
        api_key      = os.getenv("OPENAI_API_KEY", "").strip()
        self.trad_rag = TraditionalRAG()
        self.kg_rag   = KGRag()
        self.llm      = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.2,
            api_key=api_key
        )
        print("[HybridRAGEngine] Ready.")

    def ingest(self, chunks: list, doc_id: str):
        print(f"[HybridRAGEngine] Ingesting {len(chunks)} chunks "
              f"(doc_id={doc_id})...")
        self.trad_rag.build_index(chunks)
        self.kg_rag.ingest_chunks(chunks, doc_id)
        print("[HybridRAGEngine] Ingestion complete.")

    def query(self, question: str, doc_id: str) -> dict:
        print(f"[HybridRAGEngine] Query: {question}")

        vector_answer, similarity = self.trad_rag.query_with_score(question)
        print(f"[HybridRAGEngine] Similarity score: {similarity:.2f}")

        if similarity < SIMILARITY_THRESHOLD:
            # Low confidence — KG only
            print("[HybridRAGEngine] Score below threshold → KG only")
            kg_answer = self.kg_rag.query(question, doc_id)
            return {
                "answer":           kg_answer,
                "mode":             "KG Only",
                "similarity_score": similarity,
                "vector_answer":    None,
                "kg_answer":        kg_answer
            }
        else:
            # High confidence — combine both
            print("[HybridRAGEngine] Score above threshold → Hybrid mode")
            kg_answer = self.kg_rag.query(question, doc_id)

            combined_content = COMBINE_PROMPT.format(
                vector_answer=vector_answer,
                kg_answer=kg_answer
            )
            messages = [
                SystemMessage(content=MEDICAL_SYSTEM_PROMPT),
                HumanMessage(content=combined_content)
            ]
            response = self.llm.invoke(messages)
            combined = response.content if hasattr(response, "content") \
                       else str(response)

            return {
                "answer":           combined,
                "mode":             "Hybrid (Vector + KG)",
                "similarity_score": similarity,
                "vector_answer":    vector_answer,
                "kg_answer":        kg_answer
            }