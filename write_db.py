import sqlite3

conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

# cursor.execute(
#     """
#         INSERT INTO estudantes (nome, idade) VALUES (?, ?)
#         """,
#         ('Ana', 22)

# )
cursor.execute(
        """
        INSERT INTO disciplinas (estudante_id, nome_discplinas) VALUES (?, ?)
        """,
    (1, "Matemática"),
)

conn.commit()
conn.close()