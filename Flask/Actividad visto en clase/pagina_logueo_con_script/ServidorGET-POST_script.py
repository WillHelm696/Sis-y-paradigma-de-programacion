# importamos lo necesario
from flask import Flask, render_template, request

# Instancia de Flask. Aplicación
app = Flask(__name__)

# Creamos nuestro primer route. '/login'
@app.route('/')
def template():
	# Renderizamos la plantilla. Formulario HTML.
	# templates/pagina_logueo_con_script.html
	return render_template("pagina_logueo_con_script.html")
    
# Definimos el route con el método GET
@app.route('/usuario',methods=['GET','POST'])
def usuario():
	if request.method == 'GET':
		nombreUser = "Por GET recibi: "+ request.args.get('nombreUser')

	if request.method == 'POST':
		nombreUser = "Por POST recibi: "+ request.form['nombreUser']

	return "<h1>Bienvenido " + nombreUser + "</h1>"

if __name__ == '__main__':
	# Iniciamos la apicación en modo debug
	app.run(debug=True)
