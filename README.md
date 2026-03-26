# 🧠 Agentic Inventory Management System

## 🚀 Overview
An autonomous AI agent that manages, queries, and analyzes warehouse inventory using natural language.

The system combines:
- Tool-calling
- Vector search (RAG)
- SQL database operations
- Fine-tuned LLM (LoRA)

---

## 🔥 Features

- Natural language → SQL query execution
- Tool-based architecture:
  - check_stock
  - update_inventory
  - generate_report
  - dynamic_query (text → SQL)
- Semantic search using ChromaDB
- Low-stock detection with reorder suggestions
- Fine-tuned LLM using LoRA
- Fully Dockerized system

---

## 🛠️ Setup Instructions

### 1. Clone the repository
### 2. Run using Docker

### 3. Output
The system will automatically execute test queries and display results.

---

## 🧠 Architecture Diagram


### 3. Output
The system will automatically execute test queries and display results.

User Query
↓
Agent (Fine-tuned LLM)
↓
| Tools Layer |
| - SQL Database (Inventory) |
| - Vector DB (Chroma) |

↓
Final Response


---

## ⚙️ Design Choices

- **LLM (TinyLlama)**  
  Chosen for efficient local execution. The system is designed to scale to larger models like Llama 3 or Mistral.

- **Vector DB (ChromaDB)**  
  Used for semantic search to handle queries like "220V power supply".

- **Agent Design (Hybrid)**  
  Combined rule-based routing with LLM reasoning to ensure reliable tool execution and avoid parsing errors common in small models.

- **Database (SQLite)**  
  Lightweight and easy to integrate within Docker.

---

## 🔬 Fine-Tuning Details

- **Model**: TinyLlama-1.1B
- **Method**: LoRA (PEFT)
- **Dataset**: Custom text-to-SQL dataset
- **Epochs**: 3
- **Batch Size**: 2

### Training Insight
Loss decreased progressively during training (~2.3 → ~1.1), indicating improved model understanding of structured queries.

---

## 💡 Example Queries

- "Check stock of laptop"
- "Update laptop to 2"
- "Which items are low stock?"
- "Do we have 220V power supply?"
- "Show items with price greater than 1000"

---

## 🐳 Docker Support

Run the entire system with:
docker-compose up --build


This starts:
- Application
- Vector DB
- All dependencies

---

## 🎯 Key Highlights

- Reliable tool execution
- Semantic search capability
- Business logic (reorder prediction)
- Lightweight fine-tuning using LoRA
- Fully containerized deployment

---

## 📌 Conclusion

This project demonstrates a complete agentic AI system integrating reasoning, database interaction, and semantic understanding in a production-ready setup.
