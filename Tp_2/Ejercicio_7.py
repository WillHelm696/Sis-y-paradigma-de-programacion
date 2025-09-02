"""
Cree un diccionario que contenga el nombre de una ciudad, el país al que
pertenece y la cantidad de habitantes que tiene. Hacer un menú iterativo que
permita al usuario realizar las siguientes operaciones:
    . Agregar ciudades
    . Eliminar ciudades
    . Indicar la cantidad de habitantes en un país en particular
    . El porcentaje de habitantes en una ciudad de acuerdo al total registrado
"""

ciudades={
"Tokio": ("Japón",37194000),
"Delhi": ("India",32941000),
"Shanghái": ("China", 29210000),
"Daca": ("Bangladesh", 23209000),
"São Paulo": ( "Brasil", 22619000),
"Ciudad de México": ("México", 22281000),
"El Cairo": ("Egipto", 22183000) ,
"Pekín": ("China", 21766000),
"Bombay" : ("India", 21296000),
"Osaka": ("Japón", 19013000)}

while True:
    
    print("1: Agregar Ciudades")
    print("2: Eliminar Ciudades")
    print("3: Numero de habitantes de un pais")
    print("4: Porcentaje de habitntes en una coudad de acuerdo a la totaliad")
    print("0 para salir")
    
    try:
        opc=int(input(">"))
        match (opc):
            case 1:
                ciudad=input("Ciudad >")
                pais=input("Pais >")
                habitantes=int(input("Habitantes >"))
                ciudades[ciudad]=(pais,habitantes)
                print(ciudades)
            case 2:
                print("Que Ciudad va a Eliminar")
                print()
                for ciudad in ciudades.keys():
                    print(ciudad)
                element=input(">")
                del (ciudades[element])
            case 3:
                print("Que pais quiere selecionar")
                print()
                for ciudad in ciudades.keys():
                    print(ciudad)   
                print()
                selecionado=input(">")
                print("Poblacion de:",ciudades[selecionado][1])

            case 4:
                total=0
                print("De que ciuad quiere saber su pocentaje")
                for ciudad in ciudades.keys():
                    print(ciudad)   
                print()
                selecionado=input(">")
                for ciudad in ciudades.values():
                    total+=ciudad[1]
                print(total,ciudades[selecionado][1])

                print ("El porcentaaje de la ciudad es",ciudades[selecionado][1]/total)
            case 0:
                break
    except:
            print("Selecione una opcion")
            print()

