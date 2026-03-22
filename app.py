import os
import sys
import uuid
import streamlit as st
from dotenv import load_dotenv

# ── Path & env setup ──────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAG_DIR  = os.path.join(BASE_DIR, "rag")
UTIL_DIR = os.path.join(BASE_DIR, "utils")

for p in [RAG_DIR, UTIL_DIR]:
    if p not in sys.path:
        sys.path.insert(0, p)

load_dotenv(os.path.join(BASE_DIR, ".env"), override=True)

# ── Validate API key ──────────────────────────────────────────────────────────
api_key = os.getenv("OPENAI_API_KEY", "").strip()
os.environ["OPENAI_API_KEY"] = api_key

from pdf_processor import extract_text_from_pdf, chunk_text  # noqa: E402
from hybrid_engine import HybridRAGEngine                    # noqa: E402

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MediSense AI",
    page_icon="🩺",
    layout="wide"
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@400;500;600&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

.stApp {
    background: linear-gradient(135deg, #0f1b2d 0%, #1a2744 40%, #0d2137 100%);
    min-height: 100vh;
}
.main-header { text-align: center; padding: 2.5rem 0 1.5rem; }
.main-header h1 {
    font-family: 'DM Serif Display', serif;
    font-size: 3rem; color: #e8f4fd;
    letter-spacing: -0.5px; margin-bottom: 0.3rem;
}
.main-header p { color: #7db4d8; font-size: 1.1rem; }

.answer-card {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(120,180,220,0.18);
    border-radius: 14px; padding: 1.5rem; margin: 1rem 0;
    color: #d6eaf8; font-size: 1rem; line-height: 1.75;
}
.mode-badge {
    display: inline-block; padding: 3px 12px; border-radius: 20px;
    font-size: 0.75rem; font-weight: 600;
    letter-spacing: 0.5px; text-transform: uppercase;
}
.badge-hybrid { background: #1e4d7b; color: #7ecbf7; }
.badge-kg     { background: #3b2260; color: #c9a8f5; }

section[data-testid="stSidebar"] {
    background: rgba(10,20,40,0.7) !important;
    border-right: 1px solid rgba(120,180,220,0.1);
}
.stTextInput input, .stTextArea textarea {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(120,180,220,0.25) !important;
    color: #d6eaf8 !important; border-radius: 10px !important;
}
.stButton > button {
    background: linear-gradient(135deg, #1565c0, #0d47a1);
    color: white; border: none; border-radius: 10px;
    padding: 0.6rem 2rem; font-weight: 600; font-size: 0.95rem;
}
.stButton > button:hover { opacity: 0.88; }
.streamlit-expanderHeader {
    color: #7db4d8 !important; font-size: 0.85rem !important;
}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
  <h1>🩺 MediSense AI</h1>
  <p>Upload your medical report — get a plain-language explanation instantly</p>
</div>
""", unsafe_allow_html=True)

# ── API key warning ───────────────────────────────────────────────────────────
if not api_key or not api_key.startswith("sk-"):
    st.error("❌ Invalid or missing OPENAI_API_KEY in .env file. "
             "Check there are no spaces or newlines around the key.")
    st.stop()

# ── Session state ─────────────────────────────────────────────────────────────
if "engine"       not in st.session_state:
    st.session_state.engine       = HybridRAGEngine()
if "doc_id"       not in st.session_state:
    st.session_state.doc_id       = None
if "ready"        not in st.session_state:
    st.session_state.ready        = False
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ── Layout ────────────────────────────────────────────────────────────────────
col_left, col_right = st.columns([1, 2], gap="large")

with col_left:
    st.markdown("### 📂 Upload Report")
    uploaded = st.file_uploader(
        "Drop your PDF medical report here",
        type=["pdf"],
        label_visibility="collapsed"
    )

    if uploaded:
        with st.spinner("🔬 Processing document..."):
            text   = extract_text_from_pdf(uploaded)
            chunks = chunk_text(text)

            if not chunks:
                st.error("❌ Could not extract text from PDF. "
                         "Please try a different file.")
            else:
                doc_id = str(uuid.uuid4())[:8]
                st.session_state.engine.ingest(chunks, doc_id)
                st.session_state.doc_id       = doc_id
                st.session_state.ready        = True
                st.session_state.chat_history = []
                st.success(f"✅ Ready — {len(chunks)} chunks indexed")

    st.markdown("---")
    st.markdown("### ℹ️ How it works")
    st.markdown("""
    <div style='color:#7db4d8; font-size:0.85rem; line-height:1.8'>
    1. PDF → chunked text<br>
    2. Indexed in <b>FAISS</b> + <b>Neo4j</b><br>
    3. Vector similarity checked<br>
    4. &lt;30% → KG only<br>
    5. ≥30% → Vector + KG merged<br>
    6. GPT-4o-mini explains simply
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("### 💬 Ask about your report")

    if st.session_state.ready:
        st.markdown(
            "<p style='color:#7db4d8;font-size:0.82rem'>Quick questions:</p>",
            unsafe_allow_html=True
        )
        q_cols = st.columns(3)
        suggestions = [
            "What are the key findings?",
            "Are there any abnormal values?",
            "What should I discuss with my doctor?"
        ]
        for i, sug in enumerate(suggestions):
            if q_cols[i].button(sug, key=f"sug_{i}", use_container_width=True):
                st.session_state.pending_question = sug

    question = st.text_input(
        "Your question",
        placeholder="e.g. What does my cholesterol level mean?",
        label_visibility="collapsed",
        key="question_input"
    )

    if "pending_question" in st.session_state:
        question = st.session_state.pending_question
        del st.session_state.pending_question

    ask_btn = st.button("Ask →")

    if ask_btn and question and st.session_state.ready:
        with st.spinner("🧠 Analyzing..."):
            result = st.session_state.engine.query(
                question, st.session_state.doc_id
            )
            st.session_state.chat_history.append({
                "question": question,
                "result":   result
            })
    elif ask_btn and not st.session_state.ready:
        st.warning("⚠️ Please upload a medical report first.")

    for item in reversed(st.session_state.chat_history):
        res       = item["result"]
        badge_cls = "badge-hybrid" if "Hybrid" in res["mode"] else "badge-kg"

        st.markdown(f"**Q: {item['question']}**")
        st.markdown(
            f'<span class="mode-badge {badge_cls}">{res["mode"]}</span> '
            f'<span style="color:#7db4d8;font-size:0.8rem">'
            f'similarity: {res["similarity_score"]:.0%}</span>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="answer-card">{res["answer"]}</div>',
            unsafe_allow_html=True
        )

        with st.expander("🔍 See raw sources"):
            if res["vector_answer"]:
                st.markdown("**Vector RAG answer:**")
                st.info(res["vector_answer"])
            st.markdown("**KG RAG answer:**")
            st.info(res["kg_answer"])

        st.markdown("---")