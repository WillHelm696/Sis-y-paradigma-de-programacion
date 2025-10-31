from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)

CORS(app, support_credentials=True)

@app.route('/', methods=["GET", "POST"])
def funcion_servidor():
    mensaje_devuelto = "\n"

    request_data = request.get_json()
    
    for clave in request_data:
         mensaje_devuelto += clave +": "+ format(request_data[clave]) + "<br>"
        
    return jsonify({"mensaje": mensaje_devuelto})  #ESTA OPCION SIRVE PARA DEVOLVER LOS DATOS EN UN DICCIONARIO 
                                          #DE 1 ELEMENTO (identificado con la clave "mensaje") Y EL VALOR COMO UNA CADENA DE CARACTERES


@app.route('/servidor_estructura', methods=["GET", "POST"])
def funcion_servidor_estructura():
    diccionario = {}

    request_data = request.get_json()

    for clave in request_data:         
         diccionario[clave] = format(request_data[clave])
        
    diccionario['fecha_hora_servidor'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # diccionario = {}
    return jsonify(diccionario)  #ESTA OPCION SIRVE PARA DEVOLVER LOS DATOS COMO UNA ESTRUCTURA DE DATOS


@app.route('/calcular', methods=["GET", "POST"])
def calcular():
    resultado = ""

    request_data = request.get_json()
    numero1 = int(request_data['p_nro1'])
    numero2 = int(request_data['p_nro2'])
    operacion = int(request_data['p_operacion'])

    if operacion==1: #SE DEBE HACER LA SUMA
        resultado = numero1 + numero2

    if operacion==2: #SE DEBE HACER LA RESTA
        resultado = numero1 - numero2 

    return jsonify({"mensaje": resultado})  #ESTA OPCION SIRVE PARA DEVOLVER LOS DATOS COMO UNA CADENA DE CARACTERES

@app.route('/sumar', methods=["GET", "POST"])
def sumar():
    resultado = ""

    request_data = request.get_json()
    numero1 = int(request_data['p_nro1'])
    numero2 = int(request_data['p_nro2'])

    resultado = numero1 + numero2

    return jsonify({"mensaje": resultado})  #ESTA OPCION SIRVE PARA DEVOLVER LOS DATOS COMO UNA CADENA DE CARACTERES

@app.route('/restar', methods=["GET", "POST"])
def restar():
    resultado = ""

    request_data = request.get_json()
    numero1 = int(request_data['p_nro1'])
    numero2 = int(request_data['p_nro2'])

    resultado = numero1 - numero2

    return jsonify({"mensaje": resultado})  #ESTA OPCION SIRVE PARA DEVOLVER LOS DATOS COMO UNA CADENA DE CARACTERES

#LA SIGUIENTE LINEA SE UTILIZA PARA EJECUTAR EL ARCHIVO CON: py ServiciosPython.py,
#en vez de: flask --app .\ServiciosPython.py --debug run 
# AMBAS OPCIONES SIRVEN PARA VER EN EL NAVEGADOR CADA CAMBIO REALIZADO DE MANERA AUTOMATICA
if __name__ == '__main__':
     app.run(debug=True, port=5000)