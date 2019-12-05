from flask import Flask, render_template
from playhouse.shortcuts import model_to_dict, dict_to_model
import json
from trab3 import *

#Peço desculpas caso esteja algo de errado, não consigo testar em cada por não conseguir instalar todos os aparates necessários

app = Flask(__name__)
app.config['SECRET_KEY'] = "123"

@app.route("/")
def inicio():
    pessoas = list(map(model_to_dict, Campeonato.select()))
    response = jsonify({"lista": pessoas})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return render_template("index.html", dados=response)

app.run(debug=True)

'''
campeonatinho = Campeonato.select()
user_obj = campeonatinho.get()
json_data = json.dumps(model_to_dict(user_obj, manytomany=True))
print(json_data)
'''