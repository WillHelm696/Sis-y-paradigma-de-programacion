"""
Se ha establecido un programa para estimular a los alumnos, el cual consiste en
lo siguiente: si el promedio global obtenido por un alumno en el último periodo
es mayor o igual que 4, se le hará un descuento del 30% sobre la matrícula y no
se le cobrará IVA; si el promedio obtenido es menor que 4 deberá pagar la
matrícula completa, la cual debe incluir el 10% de IVA. Hacer un algoritmo que
calcule el valor a pagar si se conocen las notas finales de las 6 materias que
cursaron.
"""
matricula = float(input("Ingrese el monto de la matrícula: "))

notas = []
for i in range(1, 7):
    while True:
        try:
            nota = float(input(f"Ingrese la nota de la materia {i}: "))
            if 0 <= nota <= 10: 
                notas.append(nota)
                break
            else:
                print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Ingrese un número válido.")

promedio = sum(notas) / 6

if promedio >= 4:
    total_pagar = matricula * 0.70 
    print(f"\nPromedio: {promedio:.2f} Obtiene descuento")
else:
    total_pagar = matricula * 1.10
    print(f"\nPromedio: {promedio:.2f} No obtiene descuento")

print(f"El valor a pagar es: ${total_pagar:.2f}")
