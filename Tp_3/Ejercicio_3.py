"""
Escriba una función en Python que reciba como parámetro una frase y 1
carácter, y devuelva si ese carácter se encuentra dentro de la frase. Además de
ello, la función debe poder indicar la cantidad de palabras que hay en la frase.
"""

def frase_cadena(frase):
    cadena = []
    palabra = ""
    for caracter in frase:
        if caracter == " ":
            if palabra:
                cadena.append(palabra)
                palabra = ""
        else:
            palabra += caracter
    if palabra:
        cadena.append(palabra)
    return cadena

def se_encuentra(frase,caracter):
    cadena=frase_cadena(frase)
    for palabra in cadena:
        if caracter in palabra :
            return True
    return False

print("Ingrese Una frase")
frase=input(">")
print("Ingrese un caracter")
caracter=input(">")

print("El carracter esta dentro de la frase")
print(se_encuentra(frase.lower(),caracter.lower()))