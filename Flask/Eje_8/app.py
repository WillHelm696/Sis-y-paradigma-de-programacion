from flask import Flask, render_template,request,jsonify
from datetime import datetime, date

app=Flask(__name__)

@app.route('/')
def init():
    return render_template('Ejercicio_8.html')

######################################################################################################3
def calcular_promedio(lista_nota):
    promedio=0
    for nota in lista_nota:
        promedio += nota
    return promedio/len(lista_nota)

def nota_mayor(lista_notas):
    nota_mayor =0
    for i in range(0,len(lista_notas)):
        if lista_notas[i] > nota_mayor :
            nota_mayor= lista_notas[i]
    return nota_mayor

@app.route('/promedio_nota',methods=["POST"])
def promedio_nota():
    notas= request.get_json()
    lista_notas =[ float(notas.get('nota1')),float(notas.get('nota2')),float(notas.get('nota3')),float(notas.get('nota4')),float(notas.get('nota5'))]
    """ promedio= calcular_promedio(lista_notas) """
    promedio = sum(lista_notas) / len(lista_notas)
    """ mayor = max(lista_notas) """
    mayor = nota_mayor(lista_notas) 
    return jsonify({
        'promedio': promedio,
        'mayor' : mayor
    })
######################################################################################################3

@app.route('/veridicar_edad',methods=["POST"])
def veridicar_adultes():
    
    data = request.get_json()
    fecha_str= data.get("fecha")
    
    fecha_nacimiento = datetime.strptime(fecha_str, '%Y-%m-%d').date()
    hoy = date.today()
    
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        
    if edad >= 18 :
        mensaje = "es menor"    
    else:
        mensaje = "es mayor"
    return jsonify({'mensaje':mensaje})

######################################################################################################3

if __name__ == '__main__':
    app.run(debug=True, port=5000 )