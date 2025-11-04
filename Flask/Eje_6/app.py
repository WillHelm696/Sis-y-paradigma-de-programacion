from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('Ejercicio_6.html')

@app.route('/operaciones',methods=['GET','POST'])
def operaciones():
    resultado=None
    if request.method=='GET':
        num1=request.args.get('num1')
        num2=request.args.get('num2') 
        operacion =request.args.get('operacion')
    
    if request.method=='POST':
        num1=float(request.form['num1'])
        num2=float(request.form['num2'])
        operacion =request.form['operacion']

    if num1 != None and num2 != None : 
        if operacion == 'suma':
            resultado=num1+num2
        elif operacion == 'resta':
            resultado=num1-num2
        elif operacion == 'multiplicacion':
            resultado=num1*num2
        elif operacion == 'division' and num2 != 0:
            resultado=num1/num2
        else:
            resultado="Error division por CERO"
    else:
        resultado = "Ingrese datos por favor"

    if request.method=='POST':
        return render_template('Ejercicio_6.html', resultado_post=resultado)
    elif request.method=='GET':
        return render_template('Ejercicio_6.html', resultado_get=resultado)
    
    """     return f"el resultado es: {resultado} """

if __name__ == '__main__':
    # Iniciamos la apicación en modo debug
    app.run(debug=True)
