from flask import Flask, render_template, request, session, redirect
from Classe import Pessoa

app = Flask(__name__)

lista = []

@app.route("/")
def iniciar():
    return render_template("html.html")

@app.route("/cadastrar")
def add():
    nome = request.args.get("Nome")
    endereco = request.args.get("Endereço")
    telefone = request.args.get("Telefone")
    lista.append(Pessoa(nome, endereco, telefone))
    return redirect("/abrir_formulario")

@app.route("/abrir_formulario")
def abrir_formulario():
    return render_template("inserir_pessoas_formulario.html")

@app.route("/listar_pessoas")
def listar_pessoas():
    return render_template("listar_pessoa.html", usuario=lista)

@app.route("/mostrar_mensagem")
def mostrar_mensagem():
    return render_template("exibir_mensagem.html")

app.run(debug=True, host="0.0.0.0")
