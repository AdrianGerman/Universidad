from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField

from wtforms import validators

class CommentForm(Form):
    username = StringField ('Usuario',
                           [
                               validators.length(min=4, max=25, message="Ingresa un nombre de usuario valido"),
                               validators.Required(message = "El usuario es requerido")
                            ] )
    email = EmailField ('Correo electronico',
                            [
                               validators.Required(message = "El correo electronico es requerido")
                            ] )
    comment = TextField('Comentario',
                        [
                               validators.Required(message = "El comentario es requerido")
                        ] )    


