from flask import Flask
from flask import request

app = Flask(__name__)

#http://127.0.0.1:8000/params?params1=Adrian_German&params2=Ernesto_Becerra

@app.route('/')
def index():
    return 'Hola, Bienvenido!!'

@app.route('/saluda')
def saluda():
    return 'Hola, como te va?'

@app.route('/params')
def params():
    param = request.args.get('params1', 'no contiene este parametro')
    param_dos = request.args.get('params2', 'no contiene este parametro')
    
    return 'El parámetro es: {}, {}'. format(param, param_dos)

if __name__ == '__main__':
    app.run( debug = True, port = 8000)