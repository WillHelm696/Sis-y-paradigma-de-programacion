"""
Escribir una función que reciba una frase y devuelva un diccionario con las
palabras que contiene y su longitud.
"""

Alumnos=[("Manuel Juarez", 19823451, "Matematica"), ("Silvana Paredes", 22709128,"Programacion"), ("Rosa Ortiz", 15123978, "Redes"), ("Luciana Hernandez", 38981374, "Programacion")]

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

def diccionario_con_longitud(frase):
    frase=frase_cadena(frase)
    frase_dic={}
    for palabra in frase:
        frase_dic[palabra]=len(palabra)

    return frase_dic

print("Ingrese Una Frase")
frase=input(">")
print("Dicionario de la frase")
print(diccionario_con_longitud(frase))