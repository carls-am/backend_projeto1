import sqlite3

def conectar_dados():
    conexao = sqlite3.connect("biblioteca3.db")
    conexao.row_factory = sqlite3.Row
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao
