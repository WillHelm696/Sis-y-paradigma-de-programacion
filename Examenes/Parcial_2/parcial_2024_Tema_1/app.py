from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('parcial.html')


@app.route('/calcular_credito', methods=['POST'])
def calcular_credito():
    datos = request.get_json()
    ingresos = float(datos.get('ingresos', 0))
    valor_auto = float(datos.get('valor_auto', 0))

    # Determinar porcentaje del crédito
    if ingresos > 30000000:
        credito_max = ingresos * 0.40
    else:
        credito_max = ingresos * 0.30

    # Validar si califica
    if credito_max > valor_auto * 0.20:
        mensaje = f"No califica para el crédito de este auto. Crédito posible: ${credito_max:,.2f}"
    else:
        mensaje = f"Crédito aprobado: ${credito_max:,.2f} a pagar en 36 meses."

    return jsonify({'mensaje': mensaje})


@app.route('/calcular_promedio', methods=['POST'])
def calcular_promedio():
    datos = request.get_json()
    ingresos = float(datos.get('ingresos', 0))
    promedio = ingresos / 12
    return jsonify({'promedio': promedio})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
