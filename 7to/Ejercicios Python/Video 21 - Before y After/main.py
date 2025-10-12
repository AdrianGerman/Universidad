from ast import Pass
from email import message
from sre_constants import SUCCESS
from urllib import response
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import make_response
from flask import flash

from flask import url_for
from flask import redirect

from flask_wtf import CSRFProtect
import forms
import json

app = Flask(__name__)
app.secret_key = 'my_secret_key'
csrf = CSRFProtect(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.before_request
def before_request():
    print ('1')

@app.route('/') 
def index():
    print('2')
    if 'username' in session:
        username = session['username']
        print (username)
    title = "Index"
    return render_template('index.html', title = title)


@app.after_request
def after_request(response):
    print ('3')
    return response
    
if __name__ == '__main__':
    app.run( debug = True, port = 8000)