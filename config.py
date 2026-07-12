import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# First try Streamlit Secrets, then fall back to .env
if "GOOGLE_API_KEY" in st.secrets:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
else:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY not found. Add it to Streamlit Secrets or your .env file."
    )

genai.configure(api_key=GOOGLE_API_KEY)

CHAT_MODEL = "gemini-2.5-flash"
EMBEDDING_MODEL = "gemini-embedding-001"

APP_NAME = "Lumos AI"

MAX_RESULTS = 4