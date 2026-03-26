from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///inventory.db")

def init_db():
    with engine.connect() as conn:
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            quantity INTEGER,
            price REAL,
            threshold INTEGER,
            description TEXT
        )
        """))

        conn.execute(text("DELETE FROM inventory"))

        conn.execute(text("""
        INSERT INTO inventory (name, quantity, price, threshold, description) VALUES
        ('Laptop', 10, 50000, 5, '16GB RAM office laptop'),
        ('Power Supply 220V', 3, 2000, 2, 'Heavy-duty industrial power supply'),
        ('Keyboard', 30, 1500, 10, 'Mechanical keyboard'),
        ('Monitor', 5, 12000, 3, '24-inch display'),
        ('Mouse', 50, 500, 10, 'Wireless ergonomic mouse')
        """))

        conn.commit()