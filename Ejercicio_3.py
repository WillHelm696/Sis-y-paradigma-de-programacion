"""
Leer una secuencia de números y determinar el mayor de los pares leídos.
PD: podría ingresar números hasta que el usuario ingrese un negativo o cero.
"""

mayor=0
print("ingrese un numeros y le dire cual es el mayor termine con un numero menor a 0")
num=int(input("Num:"))
while num>0 and num!=0:
    num=int(input("Num:"))
    if num > mayor:
        mayor=num
print("El mayor de los numeros ingresado es:", mayor)


