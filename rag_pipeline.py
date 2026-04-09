import os
import hashlib
import requests
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import SentenceTransformerEmbeddings

load_dotenv()


class RAGSystem:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

        self.embeddings = SentenceTransformerEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

        # 🔐 Create hash (for caching)
        with open(pdf_path, "rb") as f:
            file_hash = hashlib.md5(f.read()).hexdigest()

        self.index_path = f"indexes/{file_hash}"

        os.makedirs("indexes", exist_ok=True)

        # 🔥 Load or create FAISS
        if os.path.exists(self.index_path):
            self.vectorstore = FAISS.load_local(
                self.index_path,
                self.embeddings,
                allow_dangerous_deserialization=True
            )
            print("✅ Loaded cached embeddings")

        else:
            loader = PyPDFLoader(pdf_path)
            documents = loader.load()

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=500,
                chunk_overlap=50
            )

            docs = splitter.split_documents(documents)

            self.vectorstore = FAISS.from_documents(docs, self.embeddings)
            self.vectorstore.save_local(self.index_path)

            print("🔥 Created new embeddings")

    def ask(self, question):
        docs = self.vectorstore.similarity_search(question, k=5)

        context = "\n\n".join([doc.page_content for doc in docs])

        # 🔥 Smart Prompt (RAG + fallback)
        prompt = f"""
You are a helpful AI.

First try to answer using the given context.
If the context does not contain enough information, you can use your own knowledge.

Context:
{context}

Question:
{question}
"""

        headers = {
            "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "llama-3.3-70b-versatile",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }

        res = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=data
        )

        return res.json()["choices"][0]["message"]["content"]