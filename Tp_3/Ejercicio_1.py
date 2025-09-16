"""
Escriba una función en Python que indique si un número está en un determinado
rango de numeros.
Ej.:
Entrada: valor=3; lim_inferior=2; lim_superior=5
Salida: True
"""
def limites(valor,lim_inferior,lim_superior):

    if lim_inferior <= valor and valor <= lim_superior:
        return True
    return False

print("Limite inferior")
lim_inferior=int(input(">"))
print("Limite Superior")
lim_superior=int(input(">"))

print ("Valor")
valor=int(input(">"))

print("El valor esta dentro de los limites")
print(limites(valor, lim_inferior, lim_superior))