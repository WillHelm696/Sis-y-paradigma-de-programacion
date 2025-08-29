"""
Elabore un programa que sume números ingresados por el usuario y que su
ejecución finalice cuando la suma de los números sea mayor a 50 o bien cuando
la cantidad de números ingresados sea mayor a 10. Cuando se cumple alguna de
las condiciones de finalización, se debe mostrar la suma de todos los números.
"""

sum=0
num=0
print("Ingrese hasta 10  Numeros y le dire las suma")

for n in range(0,10):
    num=int(input("Numero:"))
    sum+=num
    if sum >50:
        print("La suma ya supero los 50 es",sum)
        break
print("La suma de Numeros es ",sum)

