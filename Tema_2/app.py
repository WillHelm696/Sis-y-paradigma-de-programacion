from flask import Flask,render_template,request,jsonify

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('parcial.html')


@app.route('/calcular_impuesto',methods=['POST'])
def calcular_impuesto():
    datos = request.get_json()
    inmueble=int(datos.get("inmueble"))
    valor=float(datos.get("valor"))
    
    impuesto = 0 
    if inmueble > 2:
        impuesto=valor*0.045
    else:
        impuesto=valor*0.03


    return jsonify({
        'impuesto':impuesto

        })

@app.route('/calcular_promedio_propiedades',methods=['POST'])
def calcular_promedio_propiedades():
    datos = request.get_json()
    inmueble=int(datos.get("inmueble"))
    valor=float(datos.get("valor"))
    

    if inmueble > 0:
        promedio= valor/inmueble
    else:
        promedio = 0.0

    return jsonify({
        'promedio':promedio
    })

if __name__ == '__main__':
    app.run(debug=True,port=5000)
