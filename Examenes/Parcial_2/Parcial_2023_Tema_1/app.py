from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('parcial.html')

@app.route('/calcular_credito', methods=['POST'])
def calcular_credito():
    data = request.json
    personas = data['personas']
    sueldos = data['sueldos']
    promedio = sum(sueldos) / len(sueldos)

    if personas > 2:
        monto = 0.7 * promedio
    else:
        monto = 2 * sum(sueldos)

    return jsonify({"monto": round(monto, 2)})

@app.route('/calcular_promedio', methods=['POST'])
def calcular_promedio():
    data = request.json
    sueldos = data['sueldos']
    promedio = sum(sueldos) / len(sueldos)

    return jsonify({"promedio": round(promedio, 2)})

if __name__ == '__main__':
    app.run(debug=True)
