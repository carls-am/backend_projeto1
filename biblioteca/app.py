from flask import Flask, jsonify
from routes.autores import autores_bp
from routes.livros import livros_bp

app = Flask(__name__)

app.register_blueprint(autores_bp)
app.register_blueprint(livros_bp)

@app.route("/")
def inicio():
    return jsonify({"Aviso: API de Biblioteca"})

if __name__ == "__main__":
    app.run(debug=True)