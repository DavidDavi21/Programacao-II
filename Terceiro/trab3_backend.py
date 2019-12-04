from flask import Flask, render_template
from playhouse.shortcuts import model_to_dict, dict_to_model
import json
from trab3 import *


app = Flask(__name__)
app.config['SECRET_KEY'] = "123"


@app.route("/")
def inicio():
    pessoas = list(map(model_to_dict, Campeonato.select()))
    response = jsonify({"lista": pessoas})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

app.run(debug=True)

'''
campeonatinho = Campeonato.select()
user_obj = campeonatinho.get()
json_data = json.dumps(model_to_dict(user_obj, manytomany=True))
print(json_data)
'''