from pickle import FALSE
from flask import Flask, jsonify, render_template, redirect, url_for, session
from flask import request

app = Flask(__name__)
app.secret_key = "llave"


# Creamos nuestro primer route. '/login'
@app.route('/login')
def login():
	return render_template("pagina_logueo_poa.html")

@app.route('/carga_operaciones_poa')
def carga_operaciones_poa():
    try:
        esta_logueado = session['logueado']
        return render_template("operaciones_poa.html")
    
    except KeyError:
        return ("NO ESTA LOGUEADO")
        

@app.route('/logueo', methods=["GET", "POST"])
def logueo():

    session['logueado'] = False
    resultado = ""
    usuarios = {"pedro":"pedro_123","juan":"juan_123","jose":"jose_123","jesus":"jesus_321","lucas":"lucas_321"}

    request_data = request.get_json()

    usuario_ingresado = request_data['p_nombre'].lower()
    clave_ingresada = request_data['p_clave'].lower()
    esta = 0
    mensaje = "OK"
    for usuario in usuarios:
        if usuario == usuario_ingresado:
            esta = 1
            if clave_ingresada != usuarios[usuario]:
                mensaje = "LA CLAVE INGRESADA ES INCORRECTA"

    if esta == 0:
        mensaje = "EL USUARIO NO EXISTE"

    if mensaje == 'OK':
        session['logueado'] = True

    return jsonify({"mensaje_devuelto": mensaje}) 


@app.route('/calcular', methods=["GET", "POST"])
def calcular():

    try:
        esta_logueado = session['logueado']

        if esta_logueado:
             
            request_data = request.get_json()
            numero1 = int(request_data['p_nro1'])
            numero2 = int(request_data['p_nro2'])
            operacion = int(request_data['p_operacion'])

            if operacion==1: #SE DEBE HACER LA SUMA
                resultado = numero1 + numero2

            if operacion==2: #SE DEBE HACER LA RESTA
                resultado = numero1 - numero2 

            return jsonify({"mensaje": resultado})  #ESTA OPCION SIRVE PARA DEVOLVER LOS DATOS COMO UNA CADENA DE CARACTERES

    except KeyError:
        resultado = "NO EXISTE LA SESION"
        return jsonify({"mensaje": str(resultado)})


#LA SIGUIENTE LINEA SE UTILIZA PARA EJECUTAR EL ARCHIVO CON: py ServiciosPython.py,
#en vez de: flask --app .\ServiciosPython.py --debug run 
# AMBAS OPCIONES SIRVEN PARA VER EN EL NAVEGADOR CADA CAMBIO REALIZADO DE MANERA AUTOMATICA
if __name__ == '__main__':
     app.run(debug=True, port=5000)