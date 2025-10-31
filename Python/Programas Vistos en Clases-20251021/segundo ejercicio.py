numero = int(input("INGRESE UN NUMERO"))
while numero<0:
    numero = int(input("INGRESE UN NUMERO"))

print("El numero ingresado es:", numero)
suma = 0
for indice in range(0,numero+1):
    suma = suma + indice
    print (indice,end=', ')

print("La suma es:", suma)