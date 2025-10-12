from wtforms import Form
from wtforms import StringField,TextAreaField
from wtforms import HiddenField
from wtforms import EmailField
from wtforms import PasswordField
from wtforms import validators
from models import User

def length_honeypot(form, field):
  if len(field.data) > 0:
    raise validators.ValidationError('El campo debe estar vacío')

class CommentForm(Form):
    username = StringField('Username', 
            [
             validators.DataRequired(message='El username es requerido'),
             validators.length(min=4, max=25, message='Ingresa un username válido')
             ])
    email = EmailField('Correo electrónico',
            [
             validators.DataRequired(message='El email es requerido'),
             validators.Email(message='Ingrese un email válido')
             ])
    comment = TextAreaField('Comentario')
    honeypot = HiddenField('', [length_honeypot])

class LoginForm(Form):
    username = StringField('Username', 
            [
             validators.DataRequired(message='El username es requerido'),
             validators.length(min=4, max=25, message='Ingresa un username válido')
             ])
    password = PasswordField('Password', [validators.DataRequired(message='El password es requerido')])

class CreateForm(Form):
  username = StringField('Username',
            [validators.DataRequired(message = 'El username es requerido'),
            validators.length(min=4, max=50, message='Ingrese un username válido')])
  email = EmailField('E-mail',
            [validators.DataRequired(message='El email es requerido'),
            validators.Email(message='Ingrese un email válido'),
            validators.length(min=4, max=50, message='Ingrese un email válido')])
  password = PasswordField('Password',
            [validators.DataRequired(message='El password es requerido')])

  def validate_username(form, field):
    username = field.data
    user = User.query.filter_by(username = username).first()
    if user is not None:
      raise validators.ValidationError('El username ya existe')
      