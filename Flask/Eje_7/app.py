from flask import Flask,render_template, request,jsonify
from flask_cors import CORS

app = Flask(__name__)

RANGO_GLOBULOS_ROJOS = (4.0, 6.0)     # millones/mm³
RANGO_GLOBULOS_BLANCOS = (4.5, 11.0) # miles/mm³
RANGO_TRIGLICERIDOS = (50, 150)      # mg/dL
COLESTEROL_LIMITE = 200

CORS(app, support_credentials=True)

@app.route('/')
def inicio():
    return render_template('Ejercicio_7.html')

# Endpoint 1: Colesterol ALTO (valor > COLESTEROL_LIMITE)
@app.route('/analisis_globulos', methods=['GET','POST'])
def analisis_globulos():
    datos = request.get_json()
    
    # 1. Extracción de datos
    nombre = datos.get('nombre', 'N/A')
    colesterol = float(datos.get('colesterol'))
    globulos_rojos = float(datos.get('globulosRojos'))
    globulos_blancos = float(datos.get('globulosBlancos'))

    # 2. Lógica de verificación de Glóbulos
    conclusion = []
    # Glóbulos Rojos
    if globulos_rojos < RANGO_GLOBULOS_ROJOS[0]:
        conclusion.append(f"Glóbulos Rojos ({globulos_rojos}): **POR DEBAJO** del rango normal ({RANGO_GLOBULOS_ROJOS}). <br>")
    elif globulos_rojos > RANGO_GLOBULOS_ROJOS[1]:
        conclusion.append(f"Glóbulos Rojos ({globulos_rojos}): **POR ENCIMA** del rango normal ({RANGO_GLOBULOS_ROJOS}).<br>")
    else:
        conclusion.append(f"Glóbulos Rojos ({globulos_rojos}): están en rango normal. <br>")
    # Glóbulos Blancos
    if globulos_blancos < RANGO_GLOBULOS_BLANCOS[0]:
        conclusion.append(f"Glóbulos Blancos ({globulos_blancos}): **POR DEBAJO** del rango normal ({RANGO_GLOBULOS_BLANCOS}).<br>")
    elif globulos_blancos > RANGO_GLOBULOS_BLANCOS[1]:
        conclusion.append(f"Glóbulos Blancos ({globulos_blancos}): **POR ENCIMA** del rango normal ({RANGO_GLOBULOS_BLANCOS}).<br>")
    else:
        conclusion.append(f"Glóbulos Blancos ({globulos_blancos}): están en rango normal.<br>")
    # 3. Respuesta al frontend
    return jsonify({
        'titulo': f"Análisis Foco: Glóbulos (Colesterol Alto: {colesterol} mg/dL)",
        'datos_recibidos': f"Datos Personales: {nombre}. Colesterol: {colesterol}.",
        'conclusion': conclusion,
        'tipo': 'alerta-medica'
    })

# Endpoint 2: Colesterol BAJO/NORMAL (valor <= COLESTEROL_LIMITE)
@app.route('/analisis_trigliceridos', methods=['GET','POST'])
def analisis_trigliceridos():
    datos = request.get_json()

    # 1. Extracción de datos
    nombre = datos.get('nombre', 'N/A')
    colesterol = float(datos.get('colesterol'))
    trigliceridos = float(datos.get('trigliceridos'))
    # 2. Lógica de verificación de Triglicéridos
    conclusion = []
    if trigliceridos < RANGO_TRIGLICERIDOS[0]:
        conclusion.append(f"Triglicéridos ({trigliceridos}): **POR DEBAJO** del rango normal ({RANGO_TRIGLICERIDOS}). Se considera bajo riesgo.")
        tipo_mensaje = 'exito'
    elif trigliceridos > RANGO_TRIGLICERIDOS[1]:
        conclusion.append(f"Triglicéridos ({trigliceridos}): **POR ENCIMA** del rango normal ({RANGO_TRIGLICERIDOS}). **Riesgo cardiovascular elevado.**")
        tipo_mensaje = 'alerta-medica'
    else:
        conclusion.append(f"Triglicéridos ({trigliceridos}): están en rango normal.")
        tipo_mensaje = 'exito'
    # 3. Respuesta al frontend
    return jsonify({
        'titulo': f"Análisis Foco: Triglicéridos (Colesterol Normal: {colesterol} mg/dL)",
        'datos_recibidos': f"Datos Personales: {nombre}. Triglicéridos: {trigliceridos}.",
        'conclusion': conclusion,
        'tipo': tipo_mensaje
    })

if __name__ == '__main__':
    app.run(debug=True)