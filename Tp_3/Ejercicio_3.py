"""
Escriba una función en Python que reciba como parámetro una frase y 1
carácter, y devuelva si ese carácter se encuentra dentro de la frase. Además de
ello, la función debe poder indicar la cantidad de palabras que hay en la frase.
"""

def se_encuentra(frase,caracter):
    cadena=list(frase)

    if caracter in cadena :
        return True
    return False

print("Ingrese Una frase")
frase=input(">")
print("Ingrese un caracter")
caracter=input(">")

print("El carracter esta dentro de la frase")
print(se_encuentra(frase.lower(),caracter.lower()))