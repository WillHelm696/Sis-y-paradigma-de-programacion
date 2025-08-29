"""
Leer una secuencia de 10 números, almacenarlos en una lista y mostrar la 
suma de los elementos que ocupan posiciones pares y el mayor número de los que ocupan posiciones impares. 
"""

print("Ingrese 10 Numeros")
numeros=[]
for n in range(0,10):
    x=int(input("Numero: "))
    numeros.append(x)

print("-------------------------------------------")
sum=0
mayor=0
for i,n in enumerate(numeros):
    if i%2==0:
        sum+=n
    else:
        if mayor <= n:
            mayor=n
print("suma de elementos de la posicion Par : ",sum)
print("El mayor numero de la posicion Impar : ",mayor)
