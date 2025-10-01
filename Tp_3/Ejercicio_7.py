"""
Realice el ejercicio 5 del practico número 2 (listas de tuplas), pero
implementando la/s función/es necesaria/s.

Escribir un programa que permita cargar y procesar datos de alumnos del ITU en
una lista de tuplas con la siguiente forma: (nombre, dni, materia). Ejemplo:
[(“Manuel Juarez”, 19823451, “Matematica”), (“Silvana Paredes”, 22709128,
“Programacion”), (“Rosa Ortiz”, 15123978, “Redes”), (“Luciana Hernandez”,
38981374, “Programacion”)]. Hacer un menú iterativo que permita al usuario
realizar las siguientes operaciones:
    Agregar alumnos a la lista.
    Dado el DNI de un alumno, ver las materias que cursa.
    Dada una materia, mostrar la cantidad de alumnos que la cursan.
"""

def agregar_alumno(lista):
    nombre = input("Ingrese el nombre del alumno: ")
    try:
        dni = int(input("Ingrese el DNI del alumno: "))
    except ValueError:
        print("DNI inválido. Debe ser un número.")
        return
    materia = input("Ingrese la materia que cursa: ")
    
    lista.append((nombre, dni, materia))
    print("Alumno agregado correctamente.")

def materias_por_dni(lista):
    try:
        dni = int(input("Ingrese el DNI del alumno: "))
    except ValueError:
        print("DNI inválido.")
        return

    materias = [materia for (nombre, d, materia) in lista if d == dni]
    
    if materias:
        print(f"El alumno con DNI {dni} cursa las siguientes materias:")
        for m in materias:
            print(f"- {m}")
    else:
        print("No se encontraron materias para ese DNI.")

def contar_alumnos_por_materia(lista):
    materia_buscada = input("Ingrese el nombre de la materia: ")
    alumnos_en_materia = set()

    for nombre, dni, materia in lista:
        if materia.lower() == materia_buscada.lower():
            alumnos_en_materia.add(dni)  # Evita contar el mismo alumno varias veces

    cantidad = len(alumnos_en_materia)
    print(f"{cantidad} alumno(s) cursan la materia '{materia_buscada}'.")

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Agregar alumno")
    print("2. Ver materias por DNI")
    print("3. Cantidad de alumnos por materia")
    print("4. Salir")


alumnos = [
    ("Manuel Juarez", 19823451, "Matematica"),
    ("Silvana Paredes", 22709128, "Programacion"),
    ("Rosa Ortiz", 15123978, "Redes"),
    ("Luciana Hernandez", 38981374, "Programacion")
]

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        agregar_alumno(alumnos)
    elif opcion == "2":
        materias_por_dni(alumnos)
    elif opcion == "3":
        contar_alumnos_por_materia(alumnos)
    elif opcion == "4":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")

    print("================================================================")