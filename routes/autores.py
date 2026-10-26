from flask import Blueprint, jsonify, request
from biblioteca.database import conectar_dados

autores_bp = Blueprint("autores", __name__)

@autores_bp.route("/autores", methods=["GET"])
def listar_autores():

    conexao = conectar_dados()

    livros = conexao.execute(

    ).fetchall()