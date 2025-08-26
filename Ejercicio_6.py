"""
Escribir un programa que pregunte al usuario una cantidad de dinero ($) a
invertir, el interés anual y el número de años, y muestre por pantalla el capital
obtenido en la inversión cada año que dura la inversión. Nota: el valor inicial de
cada año depende del capital + interés obtenido en el año anterior.
"""

dinero=int(input("Dinero a invertir $"))
interes=int(input("Interes Anual %"))
x=int(input("Cuantos años invertira :"))

ganansia=dinero
for n in range(1,x+1):
    ganansia += (1/interes)*ganansia
    print("Ganancia en ",n,"º año:", ganansia," ganancia de ",ganansia-dinero)
print("Su inversion de $",dinero," es de: ",ganansia)

