import sqlite3

conexao = sqlite3.connect("biblioteca.db")
conexao.execute("PRAGMA foreign_keys = ON")

try:
    cursor = sqlite3.connect("biblioteca.db")
    conexao.execute("""
    CREATE TABLE IF NOT EXISTS autores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        nacionalidade TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        ano INTEGER NOT NULL,
        autorid INTEGER NOT NULL,
        FOREIGN KEY (autorid)
            REFERENCES autores(id)
    )
    
    """)

    autores = [
        ("Machado de Assis", "Brasileiro"),
        ("J.K. Rowling", "Desgraçada"),
        ("George Orwell", "Britânico"),
        ("Jane Austen", "Britânica"),
        ("Gabriel García Márquez", "Colombiano")
    ]

    livros = [
         ("ABC da letras", 2000, "J.K. Rowling")
         ("Blibia", 2033, "Jane Austen")
         ("Segura O Tchan", 4, "Gabriel Garcia Márquez")
         ("Super mario odissey", 2000, "George Orwell")
         ("Ariana Pequena e o thank u next", 2103, "Machado de Assis")
         ("Receitas de Bolo", 2000, "Jane Austen")
    ]

    for nome, nacionalidade in autores:
        cursor.execute("""
        SELECT id FROM autores
        WHERE nome = ?
        """, (nome))

        if cursor.fetchone() is None:
                cursor.execute("""
                INSERT INTO autores (nome)
                VALUES (?, ?)""", (nome))
except:
    print("penis")