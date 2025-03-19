# Witcher Graph RAG Chatbot

This is a **Graph-based Retrieval-Augmented Generation (RAG) chatbot** built using **LightRAG** and **Gradio**. It allows users to query information about *The Last Wish* (the first Witcher book) and get AI-generated responses.

## 🚀 Features

- **Graph-based RAG** for structured knowledge retrieval.
- **OpenAI GPT-based completion** for answering queries.
- **Text preprocessing** to clean and format input data.
- **Gradio Interface** for easy interaction.
- **.env configuration** for API key management.

---

## 🛠️ **Installation & Setup**

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/witcher-graph-rag.git
cd witcher-graph-rag
```

### 2️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```
## 🔑 Setting Up Environment Variables*
1. Create a .env file in the project root:
```bash
touch .env
```
2. Add your OpenAI API key inside .env:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```
## ▶️ Running the Project
```bash
python main.py
```
