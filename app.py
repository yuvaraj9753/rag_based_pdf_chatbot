import streamlit as st
from rag_pipeline import RAGSystem

st.set_page_config(page_title="PDF RAG (Groq)", layout="wide")

# 🎨 Custom CSS
st.markdown("""
<style>
.chat-user {
    background-color: #DCF8C6;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
}
.chat-bot {
    background-color: #F1F0F0;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("📄 DocuRAG – PDF-based RAG Chatbot")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")

    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []

# Session state for chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Load RAG only once
if uploaded_file and "rag" not in st.session_state:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.session_state.rag = RAGSystem("temp.pdf")

# Chat display
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='chat-user'>🧑 {msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bot'>🤖 {msg['content']}</div>", unsafe_allow_html=True)

# Input
question = st.chat_input("Ask something about your PDF...")

if question and uploaded_file:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": question})

    with st.spinner("🤖 Thinking..."):
        answer = st.session_state.rag.ask(question)

    # Save bot message
    st.session_state.messages.append({"role": "bot", "content": answer})

    st.rerun()

elif question and not uploaded_file:
    st.warning("⚠️ Please upload a PDF first")