from flask import Flask, render_template, request, session, redirect, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "llave123"
CORS(app, supports_credentials=True)

# Usuario fijo
usuarios = {
    "admin": "1234"
}

# ------------------------------
#   LOGIN
# ------------------------------
@app.route('/')
def login_page():
    return render_template("login.html")

@app.route('/login', methods=["POST"])
def login():
    datos = request.get_json()
    user = datos["user"]
    pasw = datos["pasw"]

    if user in usuarios and usuarios[user] == pasw:
        session["contador"]=0
        session["usuario"] = user
        session["suma_cant"] = 0     # suma de cantidades
        session["suma_precios"] = 0  # suma de precios unitarios
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "message": "Usuario o clave incorrectos"})


# ------------------------------
#   PÁGINA VENTAS (PROTEGIDA)
# ------------------------------
@app.route('/ventas')
def ventas():
    if "usuario" not in session:
        return redirect("/")
    return render_template("ventas.html")


# ------------------------------
#   REGISTRAR VENTA
# ------------------------------
@app.route('/registrar', methods=["POST"])
def registrar():
    if "usuario" not in session:
        return jsonify({"success": False,"error": "No autorizado"}), 401

    datos = request.get_json()
    cantidad = float(datos["cantidad"])
    precio = float(datos["precio"])
    session["suma_cant"] += cantidad
    session["suma_precios"] += precio

    session["contador"] +=1
    return jsonify({
        "mensaje": f"Venta {session["contador"]} registrada correctamente ",
        "suma_cant": session["suma_cant"],
        "suma_precios": session["suma_precios"]
    })

# ------------------------------
#   CALCULAR PROMEDIO
# ------------------------------
@app.route('/promedio', methods=["GET"])
def promedio():
    if "usuario" not in session:
        return jsonify({"error": "No autorizado"}), 401

    if session["suma_cant"] == 0:
        return jsonify({"error": "No se registraron ventas"}), 400

    promedio = session["suma_precios"] / session["suma_cant"]

    return jsonify({
        "usuario": session["usuario"],
        "promedio": promedio
    })


# ------------------------------
#   MAIN
# ------------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)
