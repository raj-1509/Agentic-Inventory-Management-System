from sqlalchemy import text
from app.db import engine

print("TOOLS FILE LOADED")
def check_stock(item: str):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT name, quantity FROM inventory WHERE name LIKE :item"),
            {"item": f"%{item}%"}
        ).fetchall()

    return str(result)


def update_inventory(data: str):
    # expected format: "item,quantity"
    try:
        item, qty = data.split(",")
        qty = int(qty)
    except:
        return "Invalid input format. Use: product,quantity"

    with engine.connect() as conn:
        conn.execute(
            text("UPDATE inventory SET quantity = :qty WHERE name LIKE :item"),
            {"qty": qty, "item": f"%{item}%"}
        )
        conn.commit()

    return f"{item} updated to {qty}"


def generate_report():
    from sqlalchemy import text
    from app.db import engine

    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT name, quantity, threshold FROM inventory")
        ).fetchall()

    low_stock = [item for item in result if item[1] < item[2]]

    if not low_stock:
        return "All items are sufficiently stocked."

    report = "⚠️ Low stock items detected:\n\n"

    for item in low_stock:
        reorder_qty = item[2] * 2  # simple logic
        report += (
            f"{item[0]} → {item[1]} (threshold: {item[2]})\n"
            f"👉 Suggested reorder: {reorder_qty} units\n\n"
        )

    return report

def dynamic_query(query: str):
    from sqlalchemy import text
    from app.db import engine

    if "price" in query and "greater" in query:
        sql = "SELECT name, price FROM inventory WHERE price > 1000"
    else:
        return "Query not supported yet"

    with engine.connect() as conn:
        result = conn.execute(text(sql)).fetchall()

    if not result:
        return "No matching items found."

    response = "Items matching query:\n"
    for item in result:
        response += f"{item[0]} → ₹{item[1]}\n"

    return response