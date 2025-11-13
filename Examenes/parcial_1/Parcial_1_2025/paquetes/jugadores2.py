def delanteros(partidos):
    nombre_delantero=[]
    for jugador in partidos:
        if jugador['posicion']=='Delantero':
            nombre_delantero.append(jugador['nombre'])
    return nombre_delantero

def promedio_categoria(partidos,categoria):
    promedio=0
    cont=0
    for jugador in partidos:
        if jugador['categoria']==categoria:
            promedio+=jugador['edad'] 
            cont+=1
    return promedio/ cont