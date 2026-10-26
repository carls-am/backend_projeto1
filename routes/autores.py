from flask import Blueprint, jsonify, request
from biblioteca.database import conectar_banco

autores_bp = Blueprint("autores", __name__)

@autores_bp.route("/autores", methods=["GET"])
def listar_autores():

    conexao = conectar_banco()

    autores = conexao.execute(
        " "
    ).fetchall()

    conexao.close()
    return jsonify({
        dict(autor)
        for autor in autores
    })