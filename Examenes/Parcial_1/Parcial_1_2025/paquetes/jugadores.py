def cargar(partidos):
    try:
        n = int(input("Cuantos jugadores ingresara:"))

        if n>=3:
            for i in range (0,n):
                print(f"jugador {i+1} :")
                print()
                edad=int(input("edad:")) 
                nombre=input("nombre:")
                categoria=int(input("categoria primera/1, segunda/2, tercera/3:"))
                posicion=input("posicion (arquero, defensor, mediocampista, delantero):")
                estadio=input("estadio:")
                jugador={'edad': edad, 'nombre': nombre, 'categoria': categoria, 'posicion': posicion, 'estadio': estadio}

                partidos.append(jugador)
        else:
            print("Debe cargar almenos 3")

        return None
    except:
        print("Error de dato")
    return None

    
def cantidad_partidos(partidos,estadio):
    cont=0
    for jugador in partidos:
        if jugador['estadio']==estadio:
            cont+=1
    if cont == 0:
        print("El estadio No existe")
        return None
    return cont
