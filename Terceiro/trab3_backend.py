from flask import Flask, render_template
from playhouse.shortcuts import model_to_dict, dict_to_model
import json
from jsonpath_ng import jsonpath, parse
from trab3 import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "123"

campeonatinho = Campeonato.select()
user_obj = campeonatinho.get()
json_data = json.dumps(model_to_dict(user_obj, manytomany=True))
print(json_data)

'''
@app.route("/")
def inicio():
    campeonatinho = Campeonato.select()
    user_obj = campeonatinho.get()
    json_data = json.dumps(model_to_dict(user_obj, manytomany=True))
    return render_template("index.html", dados=json_data)

app.run(debug=True)
'''