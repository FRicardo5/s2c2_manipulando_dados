import sqlite3

conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

# cursor.execute(
#     """
#      SELECT * FROM estudantes
#     """
# )

cursor.execute(
    """
     SELECT * FROM disciplinas
    """
)
# estudantes = cursor.fetchall()
disciplinas = cursor.fetchall()
conn.commit()
conn.close()

for disciplina in disciplinas:
    print(disciplina)
