from flask import Blueprint, jsonify, request
from biblioteca.database import conectar_banco

livros_bp = Blueprint("autores", __name__)

@livros_bp.route("/livros", methods=["GET"])
def listar_autores():

    conexao = conectar_banco()

    livros = conexao.execute("""
        SELECT
            livros.id,
            livros.titulo,
            livros.ano,
            autores.nome AS autor,
            autores.nacionalidade
        FROM livros
        JOIN autores
        ON livros.autorid = autores.id
        ORDER BY livros.id
        """
    ).fetchall()

    conexao.close()

    resultado = []

    for livro in livros:
        resultado.append({
            "id": livro["id"],
            "nome": livro["nome"],
            "ano": livro["ano"]
        })

    return jsonify(resultado)