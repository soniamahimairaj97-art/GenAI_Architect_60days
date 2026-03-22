import os
import sys
import faiss
import numpy as np
from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# ── Path & env setup ──────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "utils"))
load_dotenv(os.path.join(BASE_DIR, ".env"), override=True)

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


class TraditionalRAG:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY", "").strip()
        self.client = OpenAI(api_key=api_key)
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.2,
            api_key=api_key
        )
        self.chunks = []
        self.index  = None
        print("[TraditionalRAG] Initialized.")

    def get_embedding(self, text: str) -> list:
        response = self.client.embeddings.create(
            input=text,
            model="text-embedding-ada-002"
        )
        return response.data[0].embedding

    def build_index(self, chunks: list):
        self.chunks = chunks
        print(f"[TraditionalRAG] Building FAISS index for {len(chunks)} chunks...")
        embeddings = [self.get_embedding(c) for c in chunks]
        dim        = len(embeddings[0])
        self.index = faiss.IndexFlatL2(dim)
        vectors    = np.array(embeddings, dtype="float32")
        self.index.add(vectors)
        print(f"[TraditionalRAG] FAISS index built. Vectors: {self.index.ntotal}")

    def query_with_score(self, question: str) -> tuple:
        if not self.chunks or self.index is None:
            return "", 0.0

        q_emb     = np.array([self.get_embedding(question)], dtype="float32")
        k         = min(4, len(self.chunks))
        distances, indices = self.index.search(q_emb, k=k)

        # OpenAI embeddings are normalized — L2 distance range is 0 to 2
        # 0 = identical match, 2 = completely opposite
        best_distance = float(distances[0][0])
        similarity    = max(0.0, 1.0 - (best_distance / 2.0))

        print(f"[TraditionalRAG] Best L2 distance: {best_distance:.4f} "
              f"| Similarity: {similarity:.2f}")

        valid_idx = [i for i in indices[0] if 0 <= i < len(self.chunks)]
        context   = "\n\n".join(self.chunks[i] for i in valid_idx)

        messages = [
            SystemMessage(content=MEDICAL_SYSTEM_PROMPT),
            HumanMessage(content=f"Context:\n{context}\n\nQuestion: {question}")
        ]
        response = self.llm.invoke(messages)

        if hasattr(response, "content"):
            return str(response.content), similarity
        return str(response), similarity