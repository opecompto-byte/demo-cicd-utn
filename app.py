from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Hola UTN! Pipeline con Python y Pruebas Unitarias (Versión 1.0)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)