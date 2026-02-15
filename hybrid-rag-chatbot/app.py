import streamlit as st
from hybrid_retriever import hybrid_search
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

# Page config
st.set_page_config(
    page_title="Hybrid RAG Chatbot",
    layout="centered"
)

st.title("Hybrid RAG Chatbot (Vector + Graph)")

# Load LLM
llm = ChatOpenAI(model="gpt-4o-mini")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Ask your question...")

if user_input:

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Retrieve context (N
