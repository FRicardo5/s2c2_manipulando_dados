import sqlite3

def conectar_db():
    conn = sqlite3.connect("escola.db")
    return conn

def criar_tabela_estudantes():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS estudantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    )
    ''')
    conn.commit()
    conn.close()

def criar_tabela_matricula():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS matricula (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        estudante_id INTEGER,s
        nome_disciplina TEXT,
        FOREIGN KEY (estudante_id) REFERENCES estudantes(id)
    )
    ''')
    conn.commit()
    conn.close()

def criar_estudantes(nome, idade):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO estudantes (nome, idade) VALUES (?, ?)
        """,
        (nome, idade)
    )
    conn.commit()
    conn.close()

def listar_estudantes():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM estudantes
        """
    )
    estudantes = cursor.fetchall()
    for estudante in estudantes:
        print(estudante)
    conn.close()

def criar_matricula(estudante_id, nome_disciplina):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO matricula (estudante_id, nome_disciplina) VALUES (?, ?)
        """,
        (estudante_id, nome_disciplina)
    )
    conn.commit()
    conn.close()

def listar_matriculas():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM matricula
        """
    )
    matriculas = cursor.fetchall()
    for matricula in matriculas:
        print(matricula)
    conn.close()