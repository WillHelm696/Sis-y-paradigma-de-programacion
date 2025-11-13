"""
Un club de futbol necesita registrar información relacionada a los jugadores que van a participar de una fecha en particular del torneo local. La información que se debe registrar es la siguiente: 
edad del jugador, nombre completo del jugador, categoría (primera, segunda, tercera), posición en la que juega (arquero, defensor, mediocampista, delantero), 
estadio donde juega. Dicha información se debe registrar en el siguiente formato:

partidos = [
    {'edad': 10, 'nombre': 'Juan Pérez', 'categoria': 1, 'posicion': 'Delantero', 'estadio': 'Malvinas Argentinas'},
    {'edad': 11, 'nombre': 'Carlos Gómez', 'categoria': 2, 'posicion': 'Mediocampista', 'estadio': 'La Bombonera'}
]

Las acciones a realizar son:

    Deberá crear un paquete con al menos 2 módulos, en los cuales se deben encontrar las funciones que resuelven los siguientes puntos.
    Carga de partidos (al menos 3).
    Mostrar la “cantidad” partidos que se juegan en un estadio en particular.
    Mostrar el nombre de todos los jugadores que juegan de delanteros.
    Mostrar el promedio de edad de los que juegan en una categoría en particular.
"""

from paquetes import jugadores as jugadores
from paquetes import jugadores2 as jugadores2
partidos = [
    {'edad': 10, 'nombre': 'Juan Pérez', 'categoria': 1, 'posicion': 'Delantero', 'estadio': 'Malvinas Argentinas'},
    {'edad': 11, 'nombre': 'Vini jr', 'categoria': 1, 'posicion': 'Delantero', 'estadio': 'Malvinas Argentinas'},
    {'edad': 9, 'nombre': 'Vizcarra Lampe', 'categoria': 1, 'posicion': 'arquero', 'estadio': 'Malvinas Argentinas'},
    
    {'edad': 12, 'nombre': 'Ramiro Suares', 'categoria': 2, 'posicion': 'Delantero', 'estadio': 'Malvinas Argentinas'},
    {'edad': 10, 'nombre': 'Jose omar', 'categoria': 3, 'posicion': 'Delantero', 'estadio': 'La Bombonera'},
    {'edad': 11, 'nombre': 'Cristian sergio', 'categoria': 2, 'posicion': 'arquero', 'estadio': 'Malvinas Argentinas'},
    
    {'edad': 11, 'nombre': 'Carlos Gómez', 'categoria': 2, 'posicion': 'Mediocampista', 'estadio': 'Malvinas Argentinas'},
    {'edad': 12, 'nombre': 'Roberto Carlos', 'categoria': 3, 'posicion': 'Delantero', 'estadio': 'La Bombonera'}
]

print("Elije una opcion")
def lista(partidos):
    for jugador in partidos:
        print(jugador)        

while True:
    print("==============================================================================")
    print("1-Carga de partidos (al menos 3).")
    print("2-Mostrar la “cantidad” partidos que se juegan en un estadio en particular.")
    print("3-Mostrar el nombre de todos los jugadores que juegan de delanteros.")
    print("4-Mostrar el promedio de edad de los que juegan en una categoría en particular.")
    print("0 Para salir")
    try:
        opc=int(input(">"))
        match (opc):
            case 1:
                jugadores.cargar(partidos)
                lista(partidos)
                print()
            case 2:
                estadio=input("Esatadio:")
                cantidad=jugadores.cantidad_partidos(partidos,estadio)
                print(f"la cantidad de jugadores en el estadio {estadio} es {cantidad}")
                print()
            case 3:
                nombres_delantero=jugadores2.delanteros(partidos)
                print(f"Los delanteros son", nombres_delantero)
                print()
            case 4:
                print("Que categoria")
                categoria=int(input(">"))
                promedio=jugadores2.promedio_categoria(partidos,categoria)
                print(f"El promedio de de la categoria {categoria} es {promedio}")
                print()
            case 0:
                break

    except:
        print("Opcion No valido")


        