from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")

def naoadicionar():
    return render_template("cadastrar.html", usuario = lista)

@app.route("/adicionar_pessoa")
def add():
    nome = request.args.get("nome")

app.run(host="0.0.0.0")