from flask import flask, render_template

app = flask(__name__)
@app.route("/")

def iniciar():
    return render_template("html.html")

app.run()
