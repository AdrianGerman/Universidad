from ast import Pass
from urllib import response
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import make_response

from flask import url_for
from flask import redirect

from flask_wtf import CSRFProtect
import forms

app = Flask(__name__)
app.secret_key = 'my_secret_key'
csrf = CSRFProtect(app)

@app.route('/') 
def index():
    if 'username' in session:
        username = session['username']
        print (username)
    title = "Index"
    return render_template('index.html', title = title)

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('login'))
    
@app.route('/login', methods = ['GET','POST']) 
def login():
    login_form = forms.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        session['username'] = login_form.username.data
    return render_template('login.html', form = login_form)

@app.route('/cookie')
def cookie():
    response = make_response( render_template('cookie.html') )
    response.set_cookie('custome_cookie ', 'Adrian')
    return response

@app.route('/comment', methods = ['GET','POST'])
def comment():
    return render_template('comment.html')
    

if __name__ == '__main__':
    app.run( debug = True, port = 8000)