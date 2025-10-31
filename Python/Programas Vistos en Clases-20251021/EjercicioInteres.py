dinero = int(input("INGRESAR EL MONTO A INVERTIR: "))
interes = int(input("INGRESAR EL INTERES ANUAL: "))
anios = int(input("INGRESAR LA CTDAD DE AÑOS A INVERTIR: "))

for indice in range(anios):
    dinero = dinero + (dinero*interes/100)
    print ("El MONTO actual es: ", dinero)