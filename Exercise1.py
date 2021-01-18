def Validacion_Usuario(usuario):
    errores = []
    if len(usuario) < 6:
        errores.append('El nombre de usuario debe contener al menos 6 caracteres.'  + '\n')
    if  len(usuario) > 12:
        errores.append("El nombre de usuario no puede contener más de 12 caracteres."  + '\n')
    if usuario.isalnum() == False:
        errores.append("El nombre de usuario puede contener solo letras y números"  + '\n')

    return errores

def Validacion_Contrasenya(contrasenya):
    errores = []
    error = 0
    if len(contrasenya) < 8:
        error = 1
    elif  contrasenya.isupper():
        error = 1
    elif  contrasenya.islower():
        error = 1
    elif  contrasenya.isdigit():
        error = 1
    elif  contrasenya.isalpha():
        error = 1
    elif  contrasenya.isalnum():
        error = 1
    elif contrasenya.find(" ") != -1:
        error = 1

    if error == 1:
        errores.append('La contraseña elegida no es segura.' + '\n')
    return errores

while True:
    errores = []
    usuario = input("Nombre de Usuario: ")
    if usuario:
        errores = Validacion_Usuario(usuario)
        if errores == []:
            print("Usuario válido")
            break
        else:
            for contador in errores:
                print(contador)
while True:
    errores = []
    contrasenya = input("Contraseña: ")
    if contrasenya:
        errores = Validacion_Contrasenya(contrasenya)
        if errores == []:
            print("Contraseña válida")
            break
        else:
            for contador in errores:
                print(contador)


