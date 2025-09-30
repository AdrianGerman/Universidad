from wtforms import Form
from wtforms import StringField
from wtforms import TextField
from wtforms import PasswordField
from wtforms import HiddenField
from wtforms import validators
from wtforms.fields.html5 import EmailField

from wtforms import validators

def length_honeypot(form, field):
       if len(field.data) > 0:
              raise validators.ValidationError('El campo debe estar vacio!!')

class CommentForm(Form):
    user = StringField ('Usuario',
                           [
                               validators.length(min=4, max=25, message="Ingresa un nombre de usuario valido"),
                               validators.Required(message = "El usuario es requerido")
                            ] )
    email = EmailField ('Correo electronico',
                            [
                               validators.Required(message = "El correo electronico es requerido")
                            ] )
    comment = TextField('Comentario')
    
    honeypot = HiddenField('', [length_honeypot])    


class LoginForm(Form):
   username = StringField('Usuario',
                          [
                             validators.Required(message = "El usuario es requerido"),
                             validators.length(min=5, max=25, message="Ingrese un usuario valido")
                          ])
   password = PasswordField('Contraseña', 
                            [ 
                             validators.Required(message = "El password es requerido")
                             ])