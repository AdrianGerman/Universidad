# Trabajo programado por Adrian Ernesto German Becerra.
def validacion_user(username):
    if (len(username) < 6):
        print ('El nombre de usuario debe contener al menos "6" caracteres')
    elif (len(username) > 12):
        print ('El nombre de usuario no puede contener más de "12" caracteres')
    elif (not username.isalnum()):
        print('El nombre de usuario puede contener solo numeros y letras')
    else:
        return True
    return False

def validacion_pass(password):
    if (len(password) < 8):
        print ('La contraseña debe tener al menos "8" caracteres')
    elif (password.isupper()):
        print ('La contraseña debe contener mayúsculas')
    elif (password.islower()):
        print('La contraseña debe contener minúsculas')
    elif (password.isdigit()):
        print('La contraseña debe contener números')
    elif (password.isalnum()):
        print('La contraseña debe contener al menos 1 caracter especial')
    elif (password.count(" ") > 0):
        print('La contraseña no debe contener espacios')
    else:
        return True
    return False
    

print('--------------------------------------------')
print('Inicio de sesión')
username = input('Ingresa nombre de usuario: ')
password = input('Ingresa contraseña: ')
print('--------------------------------------------')


if (validacion_user(username)):
    print('Nombre de usuario correcto')
    print('--------------------------------------------')
    
    
if (validacion_pass(password)):
    print('Contraseña correcta')
    print('--------------------------------------------')
else:
    print('La contraseña elegida no es segura')
    print('--------------------------------------------')

    