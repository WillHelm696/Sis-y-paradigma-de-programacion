
def validaUsuario(user):
    if 6 < len(user) and len(user)< 13:
        for i in passwd
            if i == ' ':
                print("El nombre de usuario puede contener solo letras y números")
                return False
    return True

def validaClave(passwd):
    condicion_1=False
    condicion_2=False
    condicion_3=False
    if 7 < len(passwd):
        for i in passwd
            if i.isupper() :
                condicion_1=True
            if  i.islower():
                condicion_2=True
            if i isdigit():
                condicion_3=True
            if i == ' ':
                print("La contraseña no puede contener espacions")
                return False
        if condicion_1 and condicion_2 and condicion_3 :
            print("Constraseña correcta")
        else:
            return False
    return True