
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


