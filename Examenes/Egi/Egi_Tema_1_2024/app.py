from flask import Flask, render_template, request,jsonify,session,redirect
from flask_cors import CORS

app=Flask(__name__)
CORS(app,supports_credentials=True)
app.secret_key="llave"

cuentas = {
    "maria": "maria_123",
    "carlos": "carlos_123",
    "ana": "ana_123",
    "luis": "luis_123",
    "sofia": "sofia_123",
}
# -----------------------------
# Login
# -----------------------------
@app.route('/')
def inicio():
    return render_template("login.html")

@app.route('/login',methods=['GET','POST'])
def logueo():
    session["logeado"]=False
    data = request.get_json()
    user = data.get('user')
    pasw = data.get('pasw')
    if user in cuentas and cuentas[user] == pasw:
        session["logeado"]=True
        return jsonify({"success":True})
    else:
        return jsonify({"success":False, "mensaje":"Usuario y contraseña Incorectos"})
# -----------------------------
# Página temperaturas
# -----------------------------
@app.route('/temperaturas')
def temperaturas():
    if session["logeado"]==False:
        return redirect("/")
    return render_template("temperaturas.html")
# -----------------------------
# Agregar temperatura
# -----------------------------
@app.route('/agregar_temperatura',methods=['GET','POST'])
def agregar():
    if not session["logeado"]:
        return jsonify({"success":False,"mensaje":"No ha inisiado cesion"})
    data = request.get_json()
    temp = float(data.get('temperatura'))
    session["suma_temp"] += temp
    session["contador_temp"] += 1

    return jsonify({"mensaje":"Temperatura agregada"})
# -----------------------------
# Calcular promedio
# -----------------------------
@app.route('/mostrar_promedio',methods=['GET','POST'])
def promedio():
    if not session["logeado"]:
        return jsonify({"success":False,"mensaje":"No ha inisiado cesion"})
    if session["contador_temp"] == 0:
        return jsonify ({"mensaje":"No hay temperaturas registradas"})
    promedio = session["suma_temp"] / session["contador_temp"]
    return  jsonify({"mensaje": f"Usuario: {session['usuario']}<br>Promedio: {promedio:.2f}"})

if __name__ == "__main__":
    app.run(debug=True,port=5000)