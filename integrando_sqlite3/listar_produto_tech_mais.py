import sqlite3

conn = sqlite3.connect('loja.db')
cursor = conn.cursor()

cursor.execute(
    """
        SELECT * FROM produtos
    """
)
produtos = cursor.fetchall()
conn
conn.close()
for produto in produtos:
    print(produto)

