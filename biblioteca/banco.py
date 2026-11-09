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

    for nome, nacionalidade in autores:
        cursor.execute("""
        SELECT id FROM autores
        WHERE nome = ?
        """, (nome))

        if cursor.fetchone() is None:
                cursor.execute("""
                INSERT INTO autores (nome)
                VALUES (?, ?)""", (nome))

    livros = [
         ("ABC da letras", 2000, "J.K. Rowling"),
         ("Blibia", 2033, "Jane Austen"),
         ("Segura O Tchan", 4, "Gabriel Garcia Márquez"),
         ("Super mario odissey", 2000, "George Orwell"),
         ("Ariana Pequena e o thank u next", 2103, "Machado de Assis"),
         ("Receitas de Bolo", 2000, "Jane Austen")
    ]

    for titulo, ano, nome_autor in livros:
        cursor.execute("""
        SELECT id FROM autores
        WHERE nome = ?
        """, (nome_autor))

        autor = cursor.fetchone()

        if autor is None:
            raise ValueError(f"Autor não encontrado: {nome_autor}")

        autor_id = autor[0]

        cursor.execute("""
        Select id FROM livros
        WHERE titulo = ? AND ano = ? AND autor_id = ?
        """, (titulo, ano, autor_id))

        if cursor.fetchone() is None:
            cursor.execute("""
            INSERT INTO livros (titulo, ano, autor_id)
            VALUES (?, ?, ?)
            """, (titulo, ano, autor_id))

    conexao.commit()

    print("Banco de dados salvo com sucesso (eba)")
    print(f"Autores cadastrados: {cursor.execute('SELECT COUNT(*) FROM autores').fetchone()[0]}")
    print(f"Livros cadastrados: {cursor.execute('SELECT COUNT(*) FROM livros').fetchone()[0]}")


except Exception as erro:
    conexao.rollback()
    print("Erro ao conectar com o banco de dados, morra imediatamente", erro)

finally:
    conexao.close()