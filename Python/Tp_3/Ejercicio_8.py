"""
Crea el siguiente módulo:
El módulo se denominará operaciones.py y contendrá 4 funciones para realizar
una suma, una resta, un producto y una division entre dos números. Todas
ellas devolverán el resultado.

En las funciones del módulo deberá de haber tratamiento e invocación manual
de errores para evitar que se quede bloqueada una funcionalidad, eso incluye:

    ValueError: En caso de que se envíen valores a las funciones que no sean
    números. Además deberá aparecer un mensaje que informe Error: Tipo
    de dato no válido.

    ZeroDivisionError: En caso de realizar una división por cero. Además
    deberá aparecer un mensaje que informe Error: No es posible dividir
    entre cero.
    
Una vez diseñado el modulo, desarrolle un programa que, utilizando el modulo
anterior, haga uso de todas la funciones con los parámetros ingresados por
teclado
"""

# main.py
import operaciones as op

try:
    x = input("Ingrese el primer número: ")
    y = input("Ingrese el segundo número: ")

    print(f"\nSuma: {op.suma(x, y)}")
    print(f"Resta: {op.resta(x, y)}")
    print(f"Producto: {op.producto(x, y)}")
    print(f"División: {op.division(x, y)}")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
