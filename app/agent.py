from transformers import pipeline
import re

# ✅ Import tools
from app.tools import check_stock, update_inventory, generate_report, dynamic_query
from app.vector_store import search_products

# -----------------------------
# 1. Load HuggingFace Model
# -----------------------------
pipe = pipeline(
    "text-generation",
    model="./finetuned_model",
    tokenizer="./finetuned_model",
    max_new_tokens=200,
    temperature=0.2
)
# -----------------------------
# 2. Extract Product Name
# -----------------------------
def extract_product(query: str):
    query = query.lower()

    products = ["laptop", "mouse", "keyboard", "monitor", "power supply"]

    for p in products:
        if p in query:
            return p

    return query


# -----------------------------
# 3. Extract Quantity
# -----------------------------
def extract_quantity(query: str):
    match = re.search(r"\d+", query)
    if match:
        return match.group()
    return "10"  # default


# -----------------------------
# 4. Agent Logic (FIXED ORDER)
# -----------------------------
def run_agent(query: str):
    query_lower = query.lower()
    product = extract_product(query)

    # 🔥 1. REPORT FIRST (VERY IMPORTANT)
    if "report" in query_lower or "low" in query_lower:
        return generate_report()

    # 🔹 2. STOCK CHECK
    elif "stock" in query_lower:
        return check_stock(product)

    # 🔹 3. UPDATE INVENTORY
    elif "update" in query_lower or "set" in query_lower:
        qty = extract_quantity(query)
        return update_inventory(f"{product},{qty}")

    # 🔹 4. VECTOR SEARCH (RAG)
    elif "220v" in query_lower or "power" in query_lower:
        return search_products(query)
    
    elif "price" in query_lower:
        return dynamic_query(query)
    
    # 🔹 5. FALLBACK (LLM)
    else:
        response = pipe(query)
        return response[0]["generated_text"]
