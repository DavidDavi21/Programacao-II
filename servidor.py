from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")

class Pessoa:

    def __init__(self):
        self.lista = ["Paula", "Rua 8", "3352-5253"
                     "Tiago", "Beco das Flores", "9998-7071"]

def iniciar():
    return render_template("html.html", usuario = lista)

app.run(host="0.0.0.0")
