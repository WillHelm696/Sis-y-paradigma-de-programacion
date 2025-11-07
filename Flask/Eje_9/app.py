from flask import Flask, render_template, request, jsonify

app=Flask(__name__)

@app.route('/')
def init():
    return render_template('Ejercicio_9.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)