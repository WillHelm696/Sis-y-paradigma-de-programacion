"""
Escriba una función en Python que indique si un número es perfecto. Utilice una
función auxiliar que calcule los divisores propios.
Nota: Un número perfecto es un número entero positivo que es igual a la suma
de sus divisores positivos.
Ej.:
Entrada: 6 (1+2+3)
Salida: True
"""

def numero_perfecto(n):
    x=1
    divisores=[]
    while x!=n:
        if n%x==0:
            divisores.append(x)
        x+=1
    print(divisores)
    if sum(divisores)==n:
        return True


    return False

print("INGRESE UN NUMERO")

n = int(input(">"))

print("EL NUMERO ES PERFECTO ?")
print(numero_perfecto(n))