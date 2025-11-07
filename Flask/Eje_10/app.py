from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/')
def mostrar_formulario():
    return render_template('Ejercicio_10.html')


@app.route('/analizar_globulos', methods=["POST"])
def analizar_globulos():
    data = request.get_json()
    rojos = data.get('rojos', 0)
    blancos = data.get('blancos', 0)

    mensaje = f"Datos recibidos:<br>Nombre: {data['nombre']}<br>Documento: {data['tipo_doc']}<br>"
    mensaje += f"Colesterol: {data['colesterol']}<br>Glóbulos rojos: {rojos}<br>Glóbulos blancos: {blancos}<br>"

    if rojos > 5.8:
        mensaje += "<b>Conclusión:</b> Glóbulos rojos por encima del valor normal.<br>"
    elif rojos < 4.5:
        mensaje += "<b>Conclusión:</b> Glóbulos rojos por debajo del valor normal.<br>"
    else:
        mensaje += "<b>Conclusión:</b> Glóbulos dentro del rango normal.<br>"

    mensaje += f"Fecha del análisis: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    return jsonify({"mensaje": mensaje})


@app.route('/analizar_trigliceridos', methods=["POST"])
def analizar_trigliceridos():
    data = request.get_json()
    trigliceridos = data.get('trigliceridos', 0)

    mensaje = f"Datos recibidos:<br>Nombre: {data['nombre']}<br>Documento: {data['tipo_doc']}<br>"
    mensaje += f"Colesterol: {data['colesterol']}<br>Triglicéridos: {trigliceridos}<br>"

    if trigliceridos > 150:
        mensaje += "<b>Conclusión:</b> Triglicéridos elevados. Riesgo de hipertrigliceridemia.<br>"
    else:
        mensaje += "<b>Conclusión:</b> Triglicéridos dentro de los valores normales.<br>"

    mensaje += f"Fecha del análisis: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    return jsonify({"mensaje": mensaje})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
