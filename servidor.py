from flask import Flask, render_template, request, session, redirect
from Classe import Pessoa

app = Flask(__name__)

@app.route("/")
def iniciar():
    return render_template("html.html")

@app.route("/cadastrar")
def add():
    nome = request.args.get("Nome")
    endereco = request.args.get("Endereço")
    telefone = request.args.get("telefone")
    Pessoa(nome, endereco, telefone)
    return render_template("cadastrar.html")

@app.route("/listar_pessoas")
def listar_pessoas():
    lista = [Pessoa]
    return render_template("listar_pessoas.html", usuario=lista)
    
app.run(debug=True, host="0.0.0.0")
