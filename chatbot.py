from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from config import CHAT_MODEL
from prompts import QA_PROMPT


def build_chat_chain():

    model = ChatGoogleGenerativeAI(
        model=CHAT_MODEL,
        temperature=0.3
    )

    prompt = ChatPromptTemplate.from_template(QA_PROMPT)

    chain = prompt | model | StrOutputParser()

    return chain


def ask_question(question, docs):

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    chain = build_chat_chain()

    response = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return response