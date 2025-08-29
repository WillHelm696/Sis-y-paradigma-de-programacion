"""
Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. 
Finalizar al ingresar el número 0, el cual no debe guardarse. 
Luego de que se termina la carga de la lista, solicitar al usuario otro 
número y crear una lista con los elementos de la lista original que sean menores que el número dado. 
Imprimir esta nueva lista, iterando por ella
"""
print("Crear Nueva Lista Terminar con 0")
nuemeros=[]
x=int(input("Numero: "))
while x !=0:
    nuemeros.append(x)
    x=int(input("Numero: "))

print("Sublista con numeos inferior a X termine con 0")
x=int(input("X = "))
sub=[]
while x != 0:
    sub.clear()
    for n in numeros:
        if n<x:
            sub.append(n)
    print("La lista e numeros inferior a ",x," es")
    print(sub)
    print("-------------------------")
    x=int(input("X = "))

