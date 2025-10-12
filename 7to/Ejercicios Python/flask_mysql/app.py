from flask import Flask, render_template,request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='prueba'

mysql = MySQL(app)


#sesión protegida
app.secret_key  = 'miSesionSecreta'

@app.route('/')
def index():
    query = mysql.connection.cursor()
    query.execute('SELECT * FROM departamento')
    data = query.fetchall()
    return render_template('agregarDepartamento.html',variable = data)

@app.route('/agregar', methods =['GET','POST'])
def agregar():     
	if request.method == 'POST':
		codDepartamento = request.form['codDepartamento']
		nombreDepartamento = request.form['nombreDepartamento']
		presupDepartamento = request.form['presupDepartamento']
		query = mysql.connection.cursor()
		query.execute("""INSERT INTO departamento VALUES ( %s,'%s',%s)""" %(codDepartamento,nombreDepartamento,presupDepartamento))             
		mysql.connection.commit();
		flash('Registro aregado crrectamente')
		return redirect(url_for('index'))
	    
@app.route('/eliminar/<string:id>')
def eliminar(id):
    query = mysql.connection.cursor()
    query.execute("""DELETE FROM departamento where codDepartamento  = ('%s')""" % (id))
    mysql.connection.commit();
    flash('Registro borrado crrectamente')
    return redirect(url_for('index'))


@app.route('/editar/<id>')
def editar(id):
    query = mysql.connection.cursor()
    query.execute("""SELECT * FROM departamento WHERE codDepartamento = ('%s') """ %(id))
    datoEditar = query.fetchall()
    return render_template('editar.html', datos = datoEditar[0])

@app.route('/update/<id>',methods = ['GET','POST'])
def update(id):
    if request.method == 'POST':
        codDepartamento = request.form['codDepartamento']
        nombreDepartamento = request.form['nombreDepartamento']
        presupDepartamento = request.form['presupDepartamento']
        query = mysql.connection.cursor()
        query.execute("""UPDATE departamento
                    SET
                    codDepartamento =  %s,
                    nombreDepartamento = '%s',
                    presupDepartamento = %s
                    WHERE codDepartamento = %s """%(codDepartamento,nombreDepartamento,presupDepartamento,id))
        mysql.connection.commit();
        flash('Registro se actualizó crrectamente')
        return redirect(url_for('index'))       

if __name__ == '__main__':
    app.run(port =3000, debug = True)
