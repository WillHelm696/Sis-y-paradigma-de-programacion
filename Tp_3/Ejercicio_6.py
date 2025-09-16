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
    turno=input("Ingrese turno Diurno(D)/Nocturno(N):")
    horas=int(input("Horas trabajados:"))
    dia=input("Tipo de dia Festivo(F)/Laborable(L):")
    return {"nombre":nombre,"turno":turno,"horas":horas,"dia":dia}

def presupuesto(empleado):
    
    sueldo=0
    if empleado["horas"]>0:
        if empleado["turno"].lower() == 'd':
            sueldo = 350
            if empleado["dia"].lower() == "f":
                sueldo+=350*0.10
        elif empleado["turno"].lower() == 'n':
            sueldo = 400
            if empleado["dia"].lower() == "l" :
                sueldo+=350*0.15
        sueldo = empleado["horas"]*sueldo
    else:
        print("Horas semanales No valido")
    empleado["sueldo"]=sueldo
    
def mostrar(empleado):
    print(f" {empleado["nombre"]} : {empleado["sueldo"]}")

n = int(input("¿Cuántos empleados deseas registrar? (mínimo 2): "))
if n < 2:
    print("Debes ingresar al menos 2 empleados.")

trabajadores=[]
for i in range(n):
    print()
    print("Empleado ",i+1)
    trabajadores.append(empleado())
print()

print("Sueldo de los empleados")
for emp in trabajadores:
    presupuesto(emp)
    mostrar(emp)
