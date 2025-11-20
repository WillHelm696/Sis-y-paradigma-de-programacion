from flask import Flask,render_template,request,jsonify

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('parcial.html')

@app.route('/calcular_promedio_impuesto',methods=['POST'])
def calcular_promedio_impuesto():
    datos = request.get_json()
    inmueble=int(datos.get("inmuebles"))
    valor=float(datos.get("valor"))

    abono = 0
    if inmueble>2 :
        impuesto = valor * 0.045
        abono = 0.045
    else:
        impuesto = valor * 0.03
        abono = 0.03

    return jsonify({
        'impuesto':impuesto ,
        'abono':abono
        }) 

@app.route('/calcular_promedio_propiedades',methods=['POST'])
def calcular_promedio_propiedades():
    datos = request.get_json()
    inmueble=int(datos.get("inmuebles"))
    valor=float(datos.get("valor"))

    promedio= valor/inmueble

    return jsonify({
        'promedio':promedio
        }) 

if __name__ == '__main__':
    app.run(debug=True)


