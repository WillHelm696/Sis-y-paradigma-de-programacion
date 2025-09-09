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

numeros=[10,23,56,32,56,789,3423,12,23]

print("La sublista de valores pares de",numeros,"es")
print(lista_pares(numeros))