import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter


def extract_text_from_pdf(uploaded_file) -> str:
    """Extract all text from uploaded PDF file."""
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_textpage().extractText()
    doc.close()
    return text


def chunk_text(text: str) -> list:
    """Split text into overlapping chunks for RAG indexing."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50,
        separators=["\n\n", "\n", ".", " "]
    )
    chunks = splitter.split_text(text)
    chunks = [c.strip() for c in chunks if len(c.strip()) > 30]
    print(f"[PDFProcessor] Created {len(chunks)} chunks.")
    return chunks