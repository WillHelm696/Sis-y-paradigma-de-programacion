from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('Ejercicio_6.html')



if __name__ == '__main__':
    # Iniciamos la apicación en modo debug
    app.run(debug=True)
