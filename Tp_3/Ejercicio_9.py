"""
Cree un programa que pida por teclado el ingreso de un usuario y contraseña,
luego de ello utilice las funciones validaUsuario y validaClave, ambas en un
módulo llamado seguridad. Dichas funciones deben realizar lo siguiente:

validaUsuario:

    El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12.
    El nombre de usuario debe ser alfanumérico. Si no lo cumple indicar el
        mensaje: “El nombre de usuario puede contener solo letras y números”
    Nombre de usuario válido, retorna True

validaClave:

    La contraseña debe contener un mínimo de 8 caracteres
    Una contraseña debe contener letras minúsculas, mayúsculas, números y
        al menos 1 carácter no alfanumérico
    La contraseña no puede contener espacios en blanco
    Contraseña válida, retorna True
    Contraseña no válida, retorna el mensaje: “La contraseña elegida no es segura”
"""
#from seguridad import *
import seguridad as seg
print("Usuario:")
user=input(":")
while not seg.validaUsuario(user):
    user=input(":")

print("Contraseña")
passwd=input(":")
while not seg.validaClave(passwd):
    passwd=input (":")
    

