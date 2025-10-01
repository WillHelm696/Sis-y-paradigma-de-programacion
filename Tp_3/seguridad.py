
def validaUsuario(user):
    if 6 < len(user) and len(user)< 13:
        for i in user:
            if i == ' ':
                print("El nombre de usuario puede contener solo letras y números")
                return False
    else:
        print("El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12")
        return False
    return True

def validaClave(passwd):
    
    condicion_1=False
    condicion_2=False
    condicion_3=False
    if 7 < len(passwd):
        for i in passwd:
            if i.isupper() :
                condicion_1=True
            if  i.islower():
                condicion_2=True
            if i.isdigit():
                condicion_3=True
            if i == ' ':
                print("La contraseña elegida no es segura")
                print("La contraseña no puede contener espacios")
                return False
        if (condicion_1 and condicion_2 and condicion_3)     :
            print("Constraseña valida")
            return True
        else:
            print("La contraseña elegida no es segura")
            print("Debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico")
            return False
    else:
        print("La contraseña elegida no es segura")
        print("La contraseña debe contener un mínimo de 8 caracteres")
        return False