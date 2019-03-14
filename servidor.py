from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")

def iniciar():
    return render_template("html.html")

app.run(host="0.0.0.0")
