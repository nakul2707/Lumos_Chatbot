<<<<<<< HEAD
import streamlit as st

from utils import (
    get_pdf_text,
    get_text_chunks,
    create_vector_store,
    search_documents
)

from chatbot import ask_question
from config import APP_NAME
from htmlTemplates import css


# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title=APP_NAME,
    page_icon="💡",
    layout="wide"
)

st.markdown(css, unsafe_allow_html=True)


# -------------------------
# SESSION STATE
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pdf_processed" not in st.session_state:
    st.session_state.pdf_processed = False

if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []


# -------------------------
# SIDEBAR
# -------------------------

with st.sidebar:

    st.title("💡 Lumos AI")

    st.caption(
        "Enterprise PDF Assistant powered by Gemini 2.5 Flash"
    )

    st.divider()

    uploaded_files = st.file_uploader(
        "Upload PDF Files",
        type="pdf",
        accept_multiple_files=True
    )

    if uploaded_files:

        st.success(
            f"{len(uploaded_files)} PDF(s) Selected"
        )

        if st.button(
            "⚡ Process Documents",
            use_container_width=True
        ):

            with st.spinner(
                "Reading PDFs..."
            ):

                raw_text = get_pdf_text(
                    uploaded_files
                )

                chunks = get_text_chunks(
                    raw_text
                )

                create_vector_store(
                    chunks
                )

                st.session_state.pdf_processed = True

                st.session_state.uploaded_files = [
                    pdf.name
                    for pdf in uploaded_files
                ]

            st.success(
                "PDFs processed successfully!"
            )

    st.divider()

    if st.button(
        "🗑 Clear Chat",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()

    if st.session_state.uploaded_files:

        st.divider()

        st.subheader("Uploaded PDFs")

        for file in st.session_state.uploaded_files:

            st.write(f"📄 {file}")


# -------------------------
# HEADER
# -------------------------

st.title("💡 Lumos AI")

st.caption(
    "Chat with your PDFs using Gemini 2.5 Flash"
)

st.divider()
# -------------------------
# DISPLAY CHAT HISTORY
# -------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# -------------------------
# CHAT INPUT
# -------------------------

user_question = st.chat_input(
    "Ask anything about your PDF..."
)


# -------------------------
# HANDLE QUESTION
# -------------------------

if user_question:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    # Display user message
    with st.chat_message("user"):

        st.markdown(user_question)

    # Display assistant response
    with st.chat_message("assistant"):

        # Check whether PDFs are processed
        if not st.session_state.pdf_processed:

            st.warning(
                "⚠ Please upload and process your PDFs first."
            )

        else:

            with st.spinner(
                "Thinking..."
            ):

                try:

                    docs = search_documents(
                        user_question
                    )

                    answer = ask_question(
                        user_question,
                        docs
                    )

                    st.markdown(answer)

                    # Save assistant response
                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer
                        }
                    )

                except FileNotFoundError:

                    st.error(
                        "❌ Vector database not found. Please process your PDFs again."
                    )

                except Exception as e:

                    st.error(
                        f"❌ {str(e)}"
                    )
                    # ==========================================================
# EMPTY STATE
# ==========================================================

if (
    len(st.session_state.messages) == 0
    and not st.session_state.pdf_processed
):

    st.info(
        """
## 👋 Welcome to Lumos AI

Lumos AI lets you chat with one or more PDF documents using **Google Gemini 2.5 Flash**.

### 🚀 Steps

1. Upload one or more PDFs from the sidebar.

2. Click **⚡ Process Documents**

3. Wait until processing finishes.

4. Start asking questions.

Example Questions:

• Summarize this document.

• What are the key points?

• Explain Chapter 3.

• What is the conclusion?

• List all important dates.

• Give me important interview questions from this PDF.
"""
    )

elif (
    st.session_state.pdf_processed
    and len(st.session_state.messages) == 0
):

    st.success(
        "✅ Documents processed successfully! Ask your first question."
    )


# ==========================================================
# SIDEBAR STATUS
# ==========================================================

with st.sidebar:

    st.divider()

    st.subheader("System Status")

    if st.session_state.pdf_processed:

        st.success("Vector Database Ready")

    else:

        st.warning("No Processed Documents")


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption(
    "💡 Lumos AI | Powered by Gemini 2.5 Flash | Streamlit • LangChain • FAISS"
)
# ==========================================================
# DOWNLOAD CHAT
# ==========================================================

if st.session_state.messages:

    chat_text = ""

    for message in st.session_state.messages:

        role = "You" if message["role"] == "user" else "Lumos AI"

        chat_text += f"{role}:\n{message['content']}\n\n"

    st.sidebar.divider()

    st.sidebar.download_button(
        label="📥 Download Chat",
        data=chat_text,
        file_name="lumos_chat.txt",
        mime="text/plain",
        use_container_width=True
    )


# ==========================================================
# ABOUT
# ==========================================================

with st.sidebar:

    st.divider()

    st.markdown("## 💡 About")

    st.markdown(
        """
Lumos AI is an intelligent PDF assistant powered by:

- 🤖 Gemini 2.5 Flash
- 📄 LangChain
- ⚡ FAISS Vector Search
- 🎨 Streamlit

Version: **2.0**
"""
    )


# ==========================================================
# END
# ==========================================================
=======
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from htmlTemplates import css, bot_template, user_template

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text



def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks


def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()

    response = chain({"input_documents":docs, "question": user_question}, return_only_outputs=True)

    st.session_state.chat_history.append((user_question, response["output_text"]))

    # Save chat history to file or database
    save_chat_history(st.session_state.chat_history)

def save_chat_history(chat_history):
    # Implement saving to file or database
    pass

def main():
    st.set_page_config("Chat PDF")
    st.header("Lumos⚡")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_question = st.text_input("Ask a Question from the PDF Files")

    if user_question:
        user_input(user_question)

    for user_question, bot_response in reversed(st.session_state.chat_history):
        st.markdown(
            f"""
            <div style="background-color: #454650 ; padding: 10px; border-radius: 10px; margin-bottom: 10px;">
                <div style="margin-bottom: 10px;">
                    <strong><img  src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvTNRxAKdj1QyM_mpJdf0fUxxrvimMB-ADAQ&s" style="max-height: 39px; max-width: 39px; border-radius: 50%; object-fit: cover;"></strong> {user_question}
                </div>
                <div style="background-color: #202125  ; padding: 10px; border-radius: 10px;">
                    <strong><img src="https://img.freepik.com/free-vector/graident-ai-robot-vectorart_78370-4114.jpg?size=338&ext=jpg&ga=GA1.1.2082370165.1715644800&semt=sph" style="max-height: 39px; max-width: 39px; border-radius: 50%; object-fit: cover;"></strong> {bot_response}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done")

if __name__ == "__main__":
    main()
>>>>>>> ace05383bf6b936ffedf96bf475aac8f5203b12a
