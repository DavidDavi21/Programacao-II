from flask import Flask, render_template
from Classe import Pessoa

app = Flask(__name__)

@app.route("/")
def naoadicionar():
    return render_template("html.html")

@app.route("/adicionar_pessoa")
def add():
    nome = request.args.get("nome")
    return nome

@app.route("/listar_pessoas")
def listar_pessoas():
    lista = [Pessoa("Jaoana", "Rua 21", "3333-3333")]
    return render_template("listar_pessoas.html", usuario=lista)

app.run(host="0.0.0.0")
