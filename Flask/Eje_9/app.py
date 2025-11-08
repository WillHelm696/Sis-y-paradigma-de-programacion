from flask import Flask, render_template, request, jsonify

app=Flask(__name__)

@app.route('/')
def init():
    return render_template('Ejercicio_9.html')

def ordenar_lista_string(Nombres):
    for i in range(len(Nombres)-1):
        for j in range(len(Nombres)-1-i):

            #print(Nombres[j],"Compara Con", Nombres[j+1] )

            if Nombres[j].lower() > Nombres[j+1].lower():
                aux= Nombres[j]
                Nombres[j]=Nombres[j+1]
                Nombres[j+1]= aux

@app.route('/ordenar',methods=['POST'])
def ordenar():
    datos = request.get_json()
    lista = [
        datos.get('nombre1'),
        datos.get('nombre2'),
        datos.get('nombre3'),
        datos.get('nombre4'),
        datos.get('nombre5')]
    ordenar_lista_string(lista)
    return jsonify({'nombre1':lista[0],
                    'nombre2':lista[1],
                    'nombre3':lista[2],
                    'nombre4':lista[3],
                    'nombre5':lista[4]                    
                    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)