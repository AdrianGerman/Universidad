from urllib import response
from flask import Flask
from flask import render_template
from flask import request
from flask_wtf import CSRFProtect
from flask import make_response
import forms

app = Flask(__name__)
app.secret_key = 'my_secret_key'
csrf = CSRFProtect(app)

@app.route('/') 
def index():
    custome_cookie = request.cookies.get('custome_cookies', 'Udefined')
    print (custome_cookie)
    title = "Index"
    return render_template('index.html', title = title)
    
@app.route('/login', methods = ['GET','POST']) 
def login():
    login_form = forms.LoginForm()
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