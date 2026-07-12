# 💡 Lumos AI

> An intelligent AI-powered PDF Assistant built using **Google Gemini 2.5 Flash**, **LangChain**, **FAISS**, and **Streamlit**.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.46-red?style=for-the-badge&logo=streamlit)
![Google Gemini](https://img.shields.io/badge/Google-Gemini_2.5_Flash-blue?style=for-the-badge&logo=google)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green?style=for-the-badge)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Database-orange?style=for-the-badge)

---

# 🌐 Live Demo

🚀 **Try Lumos AI Online**

**https://lumos-ai-bot.streamlit.app/**

---

# 📂 GitHub Repository

**https://github.com/nakul2707/Lumos_AI.git**

---

## 📖 Overview

Lumos AI is a **Retrieval-Augmented Generation (RAG)** based PDF assistant that enables users to upload one or multiple PDF documents and interact with them using natural language.

The application leverages **Google Gemini 2.5 Flash**, **LangChain**, **FAISS Vector Search**, and **semantic embeddings** to generate accurate, context-aware answers grounded only in the uploaded documents.

Whether you're reviewing research papers, resumes, reports, documentation, academic notes, or technical manuals, Lumos AI makes document understanding faster, smarter, and more interactive.

---

# ⭐ Key Highlights

- 📄 Chat with one or multiple PDF documents
- 🤖 Powered by Google Gemini 2.5 Flash
- 🧠 Retrieval-Augmented Generation (RAG)
- 🔍 Semantic Search using FAISS
- ⚡ Fast and context-aware responses
- 🎨 Modern Streamlit interface
- 🔒 Secure API key management using `.env`
- 📂 Modular and scalable project structure

---

# ✨ Features

- Upload multiple PDF documents
- Automatic PDF text extraction
- Intelligent text chunking
- Semantic document search
- AI-powered question answering
- Context-aware responses
- Local FAISS vector database
- Clean and responsive user interface
- Easy local deployment
- Secure environment variable support

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend Development |
| Streamlit | User Interface |
| Google Gemini 2.5 Flash | Large Language Model |
| LangChain | RAG Pipeline |
| FAISS | Vector Database |
| PyPDF2 | PDF Text Extraction |
| Python-dotenv | Environment Variable Management |

---

# 🏗 System Architecture

```text
                  User Uploads PDFs
                          │
                          ▼
                PDF Text Extraction
                     (PyPDF2)
                          │
                          ▼
                Text Chunking
                   (LangChain)
                          │
                          ▼
         Google Embeddings (text-embedding-004)
                          │
                          ▼
                 FAISS Vector Database
                          │
                          ▼
                 Similarity Search
                          │
                          ▼
             Google Gemini 2.5 Flash
                          │
                          ▼
               Context-Aware Response
```

---

# 📂 Project Structure

```text
Lumos_Chatbot/
│
├── app.py
├── chatbot.py
├── config.py
├── utils.py
├── prompts.py
├── htmlTemplates.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
└── faiss_index/
```

---

# ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/nakul2707/Lumos_Chatbot.git
```

```bash
cd Lumos_Chatbot
```

---

### Create a Virtual Environment

**Windows**

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root directory.

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

Generate your API key from:

**https://aistudio.google.com/**

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

The application will start locally at:

```text
http://localhost:8501
```

---

# 💻 How It Works

1. Upload one or multiple PDF documents.
2. Extract text from the uploaded PDFs.
3. Split the text into meaningful chunks.
4. Generate semantic embeddings for each chunk.
5. Store embeddings in a FAISS vector database.
6. Accept the user's natural language question.
7. Retrieve the most relevant document chunks.
8. Generate an accurate answer using Google Gemini 2.5 Flash.

---

# 💡 Challenges Solved

- Efficient processing of multiple PDF documents.
- Semantic retrieval using vector embeddings.
- Context-aware question answering using RAG.
- Secure API key management with environment variables.
- Modular architecture for easier maintenance and scalability.

---

# 🚀 Future Improvements

- Conversation memory
- Source citations with page numbers
- PDF highlighting
- OCR support for scanned PDFs
- Voice-based interaction
- Multi-language support
- User authentication
- Cloud deployment
- Chat export functionality
- Database integration

---

# 🔒 Security

- API keys are securely stored using `.env`
- Sensitive files are excluded using `.gitignore`
- Vector embeddings are stored locally
- No uploaded documents are permanently stored

---
