from config import MAX_RESULTS
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from config import EMBEDDING_MODEL


# -------------------------
# Read PDF Text
# -------------------------
def get_pdf_text(pdf_docs):


    text = ""

    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)

        for page in pdf_reader.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

    return text


# -------------------------
# Split Text into Chunks
# -------------------------
def get_text_chunks(text):

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=1200,
        chunk_overlap=200,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    return splitter.split_text(text)


# -------------------------
# Create Vector Store
# -------------------------
def create_vector_store(chunks):

    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL
    )

    vector_db = FAISS.from_texts(
        chunks,
        embedding=embeddings
    )

    vector_db.save_local("faiss_index")


# -------------------------
# Load Existing Vector Store
# -------------------------
def load_vector_store():

    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL
    )

    return FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )
def search_documents(question):

    db = load_vector_store()

    docs = db.similarity_search(
        question,
        k=MAX_RESULTS
    )

    return docs