import sqlite3

conn = sqlite3.connect('loja.db')
cursor = conn.cursor()

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL
        )
    """
)

cursor.execute(
    """
        INSERT INTO produtos (nome, preco) VALUES
        ('Teclado', 150.00),
        ('Mouse', 80.00),
        ('Monitor', 1200.00)
    """
)

conn.commit()
conn.close()    