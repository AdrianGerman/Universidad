from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola, Bienvenido!!'

@app.route('/params/')
@app.route('/params/<name>/')
@app.route('/params/<name>/<int:num>/')
def params(name = "valor por defecto", num = 'valor sin especificar'):    
    return 'El parámetro es: {} y {}'. format(name, num)

if __name__ == '__main__':
    app.run( debug = True, port = 8000)