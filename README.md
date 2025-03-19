# Witcher Graph RAG Chatbot

## 📌 Project Summary
This project is a **Graph-based RAG chatbot** using LightRAG and OpenAI's GPT. It allows querying knowledge extracted from *The Last Wish* book.

## 🚀 Implementation Process
1. **Data Extraction & Preprocessing**  
   - Extracted text from PDF using **PyPdf**, applied **cleaning functions** to normalize text.
   
2. **Graph RAG Initialization**  
   - Used **[LightRAG](https://github.com/HKUDS/LightRAG)** with OpenAI embeddings for knowledge storage.
   - Configured `QueryParam` for optimized retrieval.

3. **Chatbot Interface**  
   - Implemented using **Gradio** for an interactive UI.
   - Handled **query processing, logging, and error handling**.

4. **Performance Optimizations**  
   - Adjusted retrieval settings (`top_k`, `max_tokens`) for **faster responses**.

## 🧐 Key Findings
- **Graph-based retrieval improves structured responses** over simple embeddings.
- **Hybrid mode for retrieval** (`QueryParam(mode="hybrid")`) provides **best context**.
- **Reducing `top_k` to 10-20** improves query speed but loses accuracy.
- **Reducing 'max_tokens'** improves query speed and retains accuracy.

## 🚀 Features

- **Graph-based RAG** for structured knowledge retrieval.
- **OpenAI GPT-based completion** for answering queries.
- **Text preprocessing** to clean and format input data.
- **Gradio Interface** for easy interaction.

---

## 🛠️ **Installation & Setup**

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/MatejMihailovic/witcher-graph-rag.git
cd witcher-graph-rag
```

### 2️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```
## 🔑 Setting Up Environment Variables
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

## 🎯 TODOs / Future Improvements
✅ Experiment with different embedding models

✅ Fine-tune QueryParam settings for faster and more relevant responses.

✅ Add support for more books from "The Witcher" franchise.

🔲 Improve response formatting.

🔲 Add a frontend UI instead of Gradio.
