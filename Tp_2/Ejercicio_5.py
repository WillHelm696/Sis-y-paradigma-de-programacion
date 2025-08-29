"""
Escribir un programa que permita cargar y procesar datos de alumnos del ITU en
una lista de tuplas con la siguiente forma: (nombre, dni, materia). Ejemplo:
[(“Manuel Juarez”, 19823451, “Matematica”), (“Silvana Paredes”, 22709128,
“Programacion”), (“Rosa Ortiz”, 15123978, “Redes”), (“Luciana Hernandez”,
38981374, “Programacion”)]. Hacer un menú iterativo que permita al usuario
realizar las siguientes operaciones:
    . Agregar alumnos a la lista.
    . Dado el DNI de un alumno, ver las materias que cursa.
    . Dada una materia, mostrar la cantidad de alumnos que la cursan.
"""

alumnos=[("Manuel Juarez", 19823451, "Matematica"), ("Silvana Paredes", 22709128,
"Programacion"), ("Rosa Ortiz", 15123978, "Redes"), ("Luciana Hernandez",
38981374, "Programacion")]

print("Base de datos de la ITU")
cursantes=[]
while True :
    print("1-Agregar alumnos a la lista.")
    print("2-Dado el DNI de un alumno, ver las materias que cursa.")
    print("3-Dada una materia, mostrar la cantidad de alumnos que la cursan.")
    print("precione cualquier tecla para Salir")
    opc=input("opcion :")
    match (opc.int()):
        case 1:
            nombre=input("Nombre: ")
            dni=int(input("Dni: "))
            materia=input("Materia: ")
            alumnos.append((tuple[nombre, dni, materia]))
            print()
        case 2:
            dni=int(input("Dni del alumno"))
            for estudiante in alumnos:
                if estudiante[1]==dni:
                    print("Materia",estudiante[2])
        case 3:
            cursantes.clear
            materia=input("Materia: ")
            dni=int(input("Dni del alumno"))
            for estudiante in alumnos:
                if estudiante[2]==materia:
                    cursantes.append(estudiante[0])
            print(cursantes)
        case _:
            break