from flask import Flask, jsonify, request, render_template,sessions
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/')
def inicio():
    return render_template('Ejercicio_10.html')

usuarios = {"pedro":"pedro_123","juan":"juan_123","jose":"jose_123","jesus":"jesus_321","lucas":"lucas_321"}

@app.route('/crgar_banco_xxx')
def carga_operaciones_poa():
    try:
        esta_logueado = session['logueado']
        return render_template("banco_xxx.html")

    except KeyError:
        return ("NO ESTA LOGUEADO")

@app.route('/logueo', methods=["GET", "POST"])
def mostrar_formulario():
    sessions['logueado']=False
    datos=request.get_json()

    user= datos['user'].lower
    pasw=datos['pasw'].lower

    for usuario in usuario:
        if user == usuario:
            if  pasw == usuarios[user]:
                sessions['logeado']=True    
    if sessions['logueado']:
        return render_template('banco_xxx.html')
    else:
        return "Usuario y  vontraseña incorreta"


if __name__ == '__main__':
    app.run(debug=True, port=5000)

