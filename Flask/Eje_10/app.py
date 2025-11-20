from flask import Flask, jsonify, request, render_template,sessions
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/')
def mostrar_formulario():
    return render_template('Ejercicio_10.html')

usuarios = {"pedro":"pedro_123","juan":"juan_123","jose":"jose_123","jesus":"jesus_321","lucas":"lucas_321"}

@app.route('/logeo',methods=['POST','GET'])
def mostrar_formulario():
    sessions['logueado']=False
    datos=request.get_json()

    user= datos['user'].lower
    pasw=datos['pasw'].lower

    

    if sessions['logueado']:
        return render_template('banco_xxx.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)

