from langchain_text_splitters import RecursiveCharacterTextSplitter
import streamlit as st
import pdfplumber
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq                  # ← changed
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

st.header("My First Chatbot")

with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload a PDF file and start asking questions", type="pdf")

if file is not None:

    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " ", ""],
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )

    vector_store = FAISS.from_texts(chunks, embeddings)

    user_question = st.text_input("Enter your question?")

    def format_docs(docs):
        return "\n\n".join([doc.page_content for doc in docs])

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 4}
    )

    # Groq LLM - better answers!   # ← changed
    llm = ChatGroq(                 # ← changed
        model="llama-3.3-70b-versatile",     # ← changed
        api_key="sk_EtBCcJeL213fKyjkk4KsWGdyb3FYhHZhLP3hoPvUvfViYHgSDgUs" # ← changed
    )

    prompt = PromptTemplate.from_template(
    """
    Use the context below to answer the question.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """
    )

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    if user_question:
        response = chain.invoke(user_question)
        st.write(response)
