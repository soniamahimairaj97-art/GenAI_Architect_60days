import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv(override=True)

print("\n=== VECTOR DATABASE BUILDING ===")

# Load text
loader = TextLoader("data/sample.txt")
documents = loader.load()

# Split text
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print(f"Chunks created: {len(chunks)}")

# Create embeddings
embeddings = OpenAIEmbeddings()

# Store in Chroma
vectordb = Chroma.from_documents(
    chunks,
    embedding=embeddings,
    persist_directory="vector_db"
)

vectordb.persist()

print("Vector DB created successfully!")
