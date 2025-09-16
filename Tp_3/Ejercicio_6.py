"""
Los empleados de una fábrica trabajan en dos turnos, Diurno y Nocturno. Se
desea calcular el jornal diario de acuerdo a las siguientes reglas:
    La tarifa de las horas diurnas es de $350
    La tarifa de las horas nocturnas es de $400
    En caso de ser festivo, la tarifa se incrementa en un 10% en caso de turno diurno y en un 15% para el nocturno.
Desarrolle una función que permita ingresar por teclado la siguiente información
para, al menos, 2 empleados, nombre del trabajador, el número de horas
trabajadas, el turno y el tipo de día (“Festivo”, “Laborable”), para ello se podría
utilizar 1 “diccionario” para registrar la información y si los datos ingresados
son correctos llamar a otra función que realice el cálculo del sueldo a cobrar en
ese día. Mostrar por pantalla los datos ingresados y el sueldo calculado para cada
empleado.
"""
def empleado():
    nombre=input("Nombre del Empeado:")
    turno=input("ingrese turno (Diurno[D]/Nocturno[N])")
    horas=int(input("horas trabajados:"))
    dia=input("Dia (Festivo[F]/Laborable[L])")
    return {"nombre":nombre,"turno":turno,"horas":horas,"dia":dia}

def presupuesto(empleado):
    sueldo=0

    if empleado[horas]<0:
        if empleado[turno] == 'D':
            sueldo = empleado[horas]*350
            if empleado[dia] == "F":
                sueldo+=350*0.1
        elif empleado[turno] == 'N':
            sueldo = empleado[horas]*400
            if empleado[dia] == "L" :
                sueldo+=350*0.15
    else:
        print("Horas semanales No valido")
    empleado["sueldo"]=sueldo
    
def mostrar(emepleado):
    print(f" {emepleado["nombre"]} : {empleado["sueldo"]}")

trabajadores=[]
print("Ingresar Empleados")
trabajadores.append(empleado())
print("Sueldo de los empleados")

for sujeto in trabajadores:
    presupuesto(sujeto)
    mostrar(sujeto)

