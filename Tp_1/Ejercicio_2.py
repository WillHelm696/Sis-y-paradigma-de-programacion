"""
Realiza el programa necesario para determinar cuáles son los múltiplos de 5
comprendidos entre 1 y N, donde N se ingresa por teclado (controlar que N
contenga un valor positivo mayor o igual a 5).
"""

numero=int(input("Multiplos del numero 5 hasta :"))

for n in range(1,numero+1):
    if n%5==0:
        print(n)



