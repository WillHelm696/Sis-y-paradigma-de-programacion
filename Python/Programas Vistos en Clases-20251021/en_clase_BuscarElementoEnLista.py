# shopping = ['Agua', 'Huevos', 'Aceite','Naranja', 'Manzana', 'Piña']
shopping = []
producto = '-'
while producto!='0':
    producto = input("INGRESE UN PRODUCTO (0 para terminar):")
    if producto!='0':
        shopping.append(producto.upper())

elemento_a_buscar = input("INGRESE UN VALOR A BUSCAR:").upper()
while elemento_a_buscar!='':
    print ("El elemento a buscar: ",elemento_a_buscar)
    esta = 0
    indice = 0
    for elemento_lista in shopping:
        if elemento_a_buscar==elemento_lista:
            esta=1
            break
        indice+=1

    if esta==1:
        print ("El elemento: ",elemento_a_buscar," se encuentra en la posicion:",indice)
    else:
        print ("El elemento: ",elemento_a_buscar," NO se encuentra en la lista")
        
    elemento_a_buscar = input("INGRESE UN VALOR A BUSCAR:").upper()

