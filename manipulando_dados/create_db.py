import sqlite3
 
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS estudantes (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome TEXT NOT NULL,
#     idade INTEGER
# )
# ''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS disciplinas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    estudante_id INTEGER,
    nome_discplinas TEXT,
    FOREIGN KEY (estudante_id) REFERENCES estudantes(id)
)
''')

conn.commit()
conn.close()