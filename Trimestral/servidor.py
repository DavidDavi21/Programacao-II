from flask import Flask, render_template, url_for, request, session, redirect
from Classe import Pessoa
from random import randint

app = Flask(__name__)
lista = []

@app.route("/")
def start():
	return render_template("PaginaInicial.html")

@app.route("/listar_pessoas")
def listar_pessoas():
	return render_template("listar_pessoas.html", usuario=lista)

@app.route("/formulario_cadastrar")
def formulario_cadastrar():
	codigo = randint(0,1000000000)
	return render_template("formulario_cadastrar_pessoas.html", codi=codigo)

@app.route("/cadastrar")
def cadastrar():
	nome = request.args.get("nome")
	endereco = request.args.get("endereco")
	telefone = request.args.get("telefone")
	codigo = request.args.get("codigo")
	lista.append(Pessoa(nome, endereco, telefone, codigo))
	return redirect("/mensagem")

@app.route("/formulario_alterar_pessoas")
def formulario_alterar_pessoas():
	pe = None
	codigo = request.args.get("codigo")
	for pe in lista:
		if pe.codigo == codigo:
			return render_template("formulario_alterar_pessoas.html", pessoaz=pe)
		return "Pessoa não encontrada!"

@app.route("/alterar_pessoas")
def alterar_pessoas():
	nome = request.args.get("nome")
	endereco = request.args.get("endereco")
	telefone = request.args.get("telefone")
	codigo = request.args.get("codigo")
	pessoa_nova = Pessoa(nome, endereco, telefone, codigo)
	for temp in range(len(lista)):
		if lista[temp].codigo == codigo:
			lista[temp] = pessoa_nova
		return redirect("/mensagem")
	return "Algo deu errado!"

@app.route("/mensagem")
def mensagem():
	return render_template("mensagem.html")

app.run(debug=True)