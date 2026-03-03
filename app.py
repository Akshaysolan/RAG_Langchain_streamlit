import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

# ------------------ CONFIG ------------------

st.set_page_config(page_title="RAG PDF App (Groq)", layout="wide")
st.title("📄 RAG PDF Question Answering (Groq Powered)")

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("Please set GROQ_API_KEY in your .env file")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)

# ------------------ VECTOR STORE CACHE ------------------

@st.cache_resource
def create_vectorstore(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    docs = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(docs, embeddings)

    return vectorstore

# ------------------ FILE UPLOAD ------------------

uploaded_file = st.file_uploader("Upload your PDF file", type="pdf")

# ------------------ MAIN LOGIC ------------------

if uploaded_file is not None:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF uploaded successfully!")

    vectorstore = create_vectorstore("temp.pdf")

    query = st.text_input("Ask a question about the PDF")

    if query:
        with st.spinner("Generating answer..."):

            relevant_docs = vectorstore.similarity_search(query, k=3)
            context = "\n\n".join([doc.page_content for doc in relevant_docs])

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "system",
                        "content": "Answer ONLY using the provided context. If the answer is not in the context, say 'Not found in the document.'"
                    },
                    {
                        "role": "user",
                        "content": f"Context:\n{context}\n\nQuestion: {query}"
                    }
                ],
                temperature=0
            )

            answer = response.choices[0].message.content

        st.subheader("Answer:")
        st.write(answer)