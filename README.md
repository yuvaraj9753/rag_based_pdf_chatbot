# 📄 RAG-Based PDF Chatbot (Groq + LangChain)

An intelligent **Retrieval-Augmented Generation (RAG)** system that allows users to upload PDFs and ask questions in natural language. The system retrieves relevant content from the document and generates accurate answers using an LLM powered by Groq.

---

## 🚀 Features

* 📂 Upload any PDF document
* 🔍 Intelligent document search using FAISS
* 🤖 Context-aware answers using Groq LLM
* ⚡ Fast retrieval with vector embeddings
* ♻️ Smart caching (no repeated embeddings for same PDF)
* 💬 Chat-style UI (Streamlit)
* 🧠 Fallback to general knowledge if context is insufficient

---

## 🧠 How It Works

```text
PDF → Chunking → Embeddings → FAISS Index → Retrieval → Groq LLM → Answer
```

1. PDF is loaded and split into smaller chunks
2. Each chunk is converted into embeddings
3. Embeddings are stored in FAISS (vector database)
4. User query is matched with relevant chunks
5. Context + question is sent to Groq LLM
6. Final answer is generated

---

## 🛠️ Tech Stack

* **LangChain** – Document processing & pipeline
* **FAISS** – Vector database for similarity search
* **Sentence Transformers** – Text embeddings
* **Groq API** – Fast LLM inference
* **Streamlit** – UI framework
* **Python** – Core language

---

## 📁 Project Structure

```
rag_pdf_chatbot/
│
├── app.py                # Streamlit UI
├── rag_pipeline.py       # Core RAG logic
├── requirements.txt
├── .env
└── indexes/              # Cached FAISS indexes
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/rag-pdf-chatbot.git
cd rag-pdf-chatbot
```

### 2. Create virtual environment

```bash
python -m venv myvenv
myvenv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 💡 Usage

1. Upload a PDF file
2. Ask any question related to the document
3. Get instant, context-aware answers

---

## ⚠️ Notes

* First run may take time (embedding creation)
* Subsequent runs are faster due to caching
* Answers may include general knowledge if context is missing

---

## 🚀 Future Improvements

* 🔒 Strict RAG mode (only PDF-based answers)
* 📑 Show source citations (page numbers)
* 💬 Chat history persistence
* 📚 Multi-PDF support
* 🌙 Dark mode UI

---

---

## 🙌 Acknowledgements

* LangChain
* FAISS
* Sentence Transformers
* Groq

---

🔥 *Built for learning, experimentation, and real-world AI applications*
