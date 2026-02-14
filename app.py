import streamlit as st
import os
import tempfile
from dotenv import load_dotenv

# MUST be first
load_dotenv()

# Validate API key

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    st.error("OPENAI_API_KEY not found. Check your .env file")
    st.stop()

# LangChain imports AFTER env load
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma


# UI
st.title("📄 Document Upload RAG Assistant")
st.write("Upload a PDF or TXT document and ask questions.")


# Create DB folder if not exists
if not os.path.exists("chroma_db"):
    os.makedirs("chroma_db")


# Session state
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "processed" not in st.session_state:
    st.session_state.processed = False


# Upload
uploaded_file = st.file_uploader(
    "Upload document",
    type=["pdf", "txt"]
)


# Process document ONLY ONCE
if uploaded_file and not st.session_state.processed:

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        file_path = tmp.name

    st.success("File uploaded")

    # Loader
    if uploaded_file.name.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    else:
        loader = TextLoader(file_path, encoding="utf-8")

    docs = loader.load()

    # Split
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(docs)

    st.write(f"Chunks created: {len(chunks)}")

    # Embeddings
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=OPENAI_API_KEY
    )

    # Vectorstore
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

    vectorstore.persist()

    st.session_state.vectorstore = vectorstore
    st.session_state.processed = True

    st.success("Vector DB created successfully")


# Question
question = st.text_input("Ask a question from the document")


# Answer
if question and st.session_state.vectorstore:

    retriever = st.session_state.vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    docs = retriever.invoke(question)

    context = "\n\n".join([doc.page_content for doc in docs])

    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        api_key=OPENAI_API_KEY
    )

    prompt = f"""
Answer ONLY using the context below.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    st.subheader("Answer")
    st.write(response.content)


# Sidebar
st.sidebar.title("Instructions")
st.sidebar.write("""
1. Upload document  
2. Wait for processing  
3. Ask question  
4. Get answer  
""")
