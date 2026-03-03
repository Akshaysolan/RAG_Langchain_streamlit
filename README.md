# 📄 End-to-End RAG PDF Question Answering App (Groq Powered)

## 🚀 Project Overview

This project is an End-to-End Retrieval-Augmented Generation (RAG) Application built using modern LLM and vector search technologies.

## 🔧 Built With

- **Streamlit** – Frontend UI
- **LangChain** – Document processing & orchestration
- **FAISS** – Vector database
- **Sentence Transformers** – Embeddings generation
- **Groq LLM (Llama 3.x)** – Answer generation

## 🎯 What This App Does

- 📂 Upload a PDF document
- ❓ Ask questions about the PDF
- 🤖 Get AI-generated answers strictly based on the document content

## 🏗️ Architecture

User 
  ↓
Streamlit UI 
  ↓
PDF Loader 
  ↓
Text Splitter 
  ↓
Embeddings 
  ↓
FAISS Vector Store 
  ↓
Retriever 
  ↓
Groq LLM 
  ↓
Final Answer


## 🔹 Components Used

| Layer              | Tool                                   |
| ------------------ | -------------------------------------- |
| UI                 | Streamlit                              |
| PDF Parsing        | PyPDFLoader                            |
| Text Chunking      | RecursiveCharacterTextSplitter         |
| Embeddings         | sentence-transformers/all-MiniLM-L6-v2 |
| Vector Database    | FAISS                                  |
| LLM                | Groq (Llama 3.x models)                |

## 🧠 How RAG Works in This Project

1. The user uploads a PDF.
2. Text is extracted from the PDF.
3. The text is split into smaller chunks.
4. Each chunk is converted into embeddings.
5. Embeddings are stored in FAISS.
6. When a question is asked:
   - The question is converted into an embedding.
   - Similar document chunks are retrieved.
   - Retrieved context + user question is sent to the Groq LLM.
   - The model generates a final answer grounded in the document.

## 🛠️ Technologies Used

- Python 3.11
- Streamlit
- LangChain
- FAISS
- Sentence Transformers
- Groq LLM API

## 📊 Features

- ✔ Upload PDF up to 200MB
- ✔ Fast semantic search using FAISS
- ✔ Context-aware answers
- ✔ Groq-powered LLM responses
- ✔ Lightweight and efficient

## ▶️ How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

GROQ_API_KEY=your_api_key_here


**Key improvements made:**
- ✅ Proper heading hierarchy with `#` for main title and `##` for sections
- ✅ Code blocks wrapped with triple backticks for commands
- ✅ Proper bullet list formatting with `-` and sub-bullets with indentation
- ✅ Numbered lists for sequential steps
- ✅ Better organization of installation steps with sub-headings
- ✅ Improved readability and consistency


