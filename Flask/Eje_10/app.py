from flask import Flask, jsonify, request, render_template, session, url_for, redirect
from functools import wraps
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = "llave"

# Usuarios y contraseñas
usuarios = {
    "pedro": "pedro_123",
    "juan": "juan_123",
    "jose": "jose_123",
    "jesus": "jesus_321",
    "lucas": "lucas_321"
}

# Saldos iniciales
saldos = {
    "pedro": 0.0,
    "juan": 0.0,
    "jose": 0.0,
    "jesus": 0.0,
    "lucas": 0.0
}

# Actividades del usuario
actividades = {
    "pedro": "",
    "juan": "",
    "jose": "",
    "jesus": "",
    "lucas": ""
}

# ------------------------------
#   RUTA INICIO
# ------------------------------
@app.route('/')
def inicio():
    return render_template('Ejercicio_10.html')
# ------------------------------
#   DECORADOR PARA PROTEGER RUTAS
# ------------------------------
def login_requerido(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get('logueado'):
            return redirect(url_for('inicio'))
        return f(*args, **kwargs)
    return wrapper
# ------------------------------
#   LOGIN
# ------------------------------
@app.route('/login', methods=["POST"])
def login():
    datos = request.get_json()
    user = datos['user'].lower()
    pasw = datos['pasw']

    if user in usuarios and usuarios[user] == pasw:
        session['logueado'] = True
        session['usuario'] = user
        # Asignar saldo inicial predefinido si es la primera vez
        if saldos.get(user, 0.0) == 0.0:
            saldos[user] = 1000.0
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "message": "Usuario o contraseña incorrectos"})

# ------------------------------
#   PÁGINA DEL BANCO (PROTEGIDA)
# ------------------------------
@app.route('/cargar_banco_xxx')
@login_requerido
def cargar_banco_xxx():
    return render_template("banco_xxx.html")

# ------------------------------
#   API: INFO USUARIO
# ------------------------------
@app.route('/api/usuario', methods=["GET"])
def api_usuario():
    if not session.get("logueado"):
        return jsonify({"success":False,"error": "No autorizado"}), 401

    usuario = session.get("usuario")
    saldo = saldos.get(usuario, 0.0)
    return jsonify({"usuario": usuario, "saldo": saldo})

# ------------------------------
#   CERRAR SESIÓN
# ------------------------------
@app.route('/cerrar', methods=['POST'])
def cerrar_sesion():
    session.clear()
    return jsonify({"mensaje": "Sesión cerrada"}), 200

# ------------------------------
#   DEPÓSITO
# ------------------------------
@app.route('/deposito', methods=['POST'])
@login_requerido
def deposito():
    datos = request.get_json()
    monto = float(datos["monto"])

    usuario = session["usuario"]
    saldos[usuario] += monto

    actividades[usuario] = f"usuario : {usuario} deposito {monto} <br>" + actividades[usuario]
    return jsonify({"mensaje": f"Depósito exitoso +{monto}" , "saldo": saldos[usuario]})

# ------------------------------
#   RETIRO
# ------------------------------
@app.route('/retiro', methods=['POST'])
@login_requerido
def retiro():
    datos = request.get_json()
    monto = float(datos["monto"])

    usuario = session["usuario"]

    if saldos[usuario] >= monto:
        saldos[usuario] -= monto
        actividades[usuario] = f"usuario : {usuario} retitp -{monto} <br>" + actividades[usuario]
        return jsonify({"mensaje": f"Retiro exitoso -{monto}", "saldo": saldos[usuario]})
    else:
        return jsonify({"error": "Saldo insuficiente"}), 400

# ------------------------------
#   TRANSFERENCIA
# ------------------------------
@app.route('/transaccion', methods=['POST'])
@login_requerido
def transferencia():
    datos = request.get_json()
    destino = datos.get("destino", "").lower()
    monto = float(datos["monto"])    
    tipo = datos.get("tipo", "transaccion").lower()
    origen = session["usuario"]

    # Si es pago de impuestos, usamos una cuenta interna 'impuestos'
    if tipo == "impuestos":
        destino = "impuestos"
        # crear cuenta impuestos si no existe
        if destino not in saldos:
            saldos[destino] = 0.0

        if saldos[origen] < monto:
            return jsonify({"error": "Saldo insuficiente"}), 400

        saldos[origen] -= monto
        saldos[destino] += monto
        actividades[origen] = f"usuario : {origen} pago impuestos {monto} <br>" + actividades[origen]
        actividades[destino] = f"usuario : {origen} pago {monto} (impuestos) <br>" + actividades[destino]

        return jsonify({"mensaje": f"Pago de impuestos realizado -{monto}", "saldo": saldos[origen]})

    # Por defecto: transferencia entre cuentas existentes
    if destino not in saldos:
        return jsonify({"error": "Cuenta destino no existe"}), 400

    if saldos[origen] < monto:
        return jsonify({"error": "Saldo insuficiente"}), 400

    saldos[origen] -= monto
    saldos[destino] += monto
    actividades[origen] = f"usuario : {origen} transfirio {monto} a destino : {destino}<br>" + actividades[origen]
    actividades[destino] = f"usuario : {origen} transfirio {monto} a tu cuenta  <br>" + actividades[destino]

    return jsonify({"mensaje": f"Transferencia realizada -{monto}", "saldo": saldos[origen]})

# ------------------------------
#   MOVIMIENTOS (A futuro)
# ------------------------------
@app.route('/movimientos', methods=['POST'])
@login_requerido
def movimientos():
    usuario= session["usuario"]
    if actividades[usuario]=="":
        return jsonify({"mensaje": "Sin Movimientos"})
    return jsonify({"mensaje": actividades[usuario]})

# ------------------------------
#   MAIN
# ------------------------------
if __name__ == '__main__':
    app.run(debug=True, port=5000)
