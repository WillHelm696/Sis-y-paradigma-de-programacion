"""
Escriba una función en Python que reciba una lista de valores enteros y devuelva
otra lista sólo con aquellos valores pares.
Ej.:
Entrada: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Salida: [2, 4, 6, 8]
"""

def lista_pares(numeros):
    lista_pares=[]
    for i in range (0,len(numeros)):
        if numeros[i]%2==0:
            lista_pares.append(numeros[i])
    
    return(lista_pares)

print("Ingrese una serie de numeros termine con 0")
numero=int(input(">"))
colecion=[]
while numero != 0:
    colecion.append(numero)
    numero=int(input(">"))
    

print("La sublista de valores pares de",numero,"es")
print(lista_pares(colecion))