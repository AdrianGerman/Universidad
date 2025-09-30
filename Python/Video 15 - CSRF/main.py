from flask import Flask
from flask import render_template
from flask import request
from flask_wtf import CSRFProtect
import forms

app = Flask(__name__)
app.secret_key = 'my_secret_key'
csrf = CSRFProtect(app)

@app.route('/') 
def index():
    comment_form = forms.CommentForm(request.form)
    if request.method == 'POST' and comment_form.validate:
        print(comment_form.user.data)
        print(comment_form.email.data)
        print(comment_form.comment.data)
    else:
        print ('Error en el formulario')
        
    title = "Inicio"
    return render_template('index.html', title = title, form = comment_form)
    
@app.route('/login', methods = ['GET','POST']) 
def login():
    login_form = forms.LoginForm()
    return render_template('login.html', form = login_form)

@app.route('/cookie')
def cookie():
    return render_template('cookie.html')

@app.route('/comment', methods = ['GET','POST'])
def comment():
    return render_template('comment.html')
    

if __name__ == '__main__':
    app.run( debug = True, port = 8000)