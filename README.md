 # 🚀 RAG-Based Customer Support Assistant using LangGraph & HITL

## 📌 Overview

This project is an AI-powered Customer Support Assistant built using *Retrieval-Augmented Generation (RAG)*.  
It automates responses to customer queries such as refunds, shipping, cancellations, and policy-related questions using a *PDF knowledge base*.

The system retrieves relevant information using a vector database and generates accurate responses using a Large Language Model (LLM).  
It also includes a *Human-in-the-Loop (HITL)* mechanism to handle sensitive queries.

---

## 🎯 Features

- Retrieval-Augmented Generation (RAG) pipeline  
- Semantic search using ChromaDB  
- Context-aware response generation using LLM  
- PDF-based knowledge base ingestion  
- Human-in-the-Loop (HITL) escalation  
- Modular workflow using LangGraph  

---

## 🧠 System Workflow


User Query → Retrieve Relevant Chunks → LLM Processing → Generate Response → HITL Escalation (if triggered)

---

## ⚙️ Tech Stack

- *Language:* Python  
- *Frameworks:* LangChain, LangGraph  
- *Vector Database:* ChromaDB  
- *Embedding Model:* sentence-transformers/all-MiniLM-L6-v2  
- *LLM:* llama-3.1-8b-instant (Groq API)  

---

## 📂 Project Structure


<img width="218" height="457" alt="Screenshot 2026-04-23 153826" src="https://github.com/user-attachments/assets/e43b8006-11a7-4c51-bcb8-c50fea9d55dd" />


## ⚡ Installation

```bash
pip install langchain
pip install chromadb
pip install sentence-transformers
pip install groq
[8:11 am, 23/04/2026] Amma: ▶️ How to Run
Bash
python ingest.py
python app.py

🧪 Sample Queries

What is the refund policy?
How long does shipping take?
Fraud complaint

🔄 Workflow Explanation

Load PDF knowledge base
Split into chunks (size: 500, overlap: 100)
Generate embeddings
Store in ChromaDB
Retrieve relevant chunks based on query
Pass context to LLM
Generate response
Escalate sensitive queries using HITL

🚨 Human-in-the-Loop (HITL)

Sensitive queries such as fraud or complaints are detected using keyword-based logic and routed for escalation instead of generating automated responses.
🎥 Demo Video
👉 [https://drive.google.com/file/d/1k_A4yxm0qRnivwAQcN1ad0e-QJtvoTZ2/view]

📚 Key Learnings

Understanding of RAG architecture
Working with embeddings and vector databases
Designing workflows using LangGraph
Debugging real-world AI systems

⚠️ Limitations

Works only with provided PDF knowledge base
No real-time data integration
Basic HITL implementation

🚀 Future Improvements

Web-based UI (Streamlit / Flask)
Multi-document support
Chat history memory
Advanced escalation system
