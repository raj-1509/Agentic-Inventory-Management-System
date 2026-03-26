import chromadb

# Create client
client = chromadb.Client()

# Create collection safely
collection = client.get_or_create_collection(name="products")


def init_vector_db():
    docs = [
        "Laptop with 16GB RAM for office work",
        "Heavy-duty 220V industrial power supply",
        "Mechanical keyboard for typing",
        "24-inch HD monitor",
        "Wireless ergonomic mouse"
    ]

    # clear old data (important during testing)
    try:
        collection.delete(ids=[str(i) for i in range(100)])
    except:
        pass

    collection.add(
        documents=docs,
        ids=[str(i) for i in range(len(docs))]
    )


def search_products(query: str):
    results = collection.query(
        query_texts=[query],
        n_results=2
    )

    return results["documents"]