inventario = {}

opcion = 1            
while opcion != 4: 
    print("*** 1 - AGREGAR PRODUCTO") 
    print("*** 2 - VER PRODUCTOS CON STOCK MINIMO") 
    print("*** 3 - VER TODOS LOS PRODUCTOS") 
    print("*** 4 - SALIR")     
    opcion = int(input("Ingrese una Opcion: "))
    match opcion :
        case 1:
            producto = input("Ingrese el Producto: ").upper() 
            cantidades = int(input("Ingrese la Cantidad del Producto que ingreso: "))
            if (producto in inventario):
                inventario[producto]=inventario[producto] + cantidades
            else:
                inventario[producto]=cantidades
        case 2:
            for clave,valor in inventario.items():
                if valor<=10:
                    print("El Producto:", clave.upper()," tiene un stock por debajo del minimo:",valor)
        case 3:
            print("**TODOS LOS PRODUCTOS REGISTRADOS**")
            for clave,valor in inventario.items():
                    print("Producto:", clave.upper()," tiene un stock:",valor)
        case 4:
            print("*****MUCHAS GRACIAS, NOS VOLVEREMOS A VER****")
