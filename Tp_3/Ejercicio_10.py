"""
Como ejercicio, escriba una función que use la funcion tomaNumero para leer un
número del teclado y que maneje la excepción ErrorNumeroMalo.
"""
def tomaNumero():
    try:
        numero = input(":")
        if not numero.isnumeric():
            raise ValueError("El valor ingresado no es numerico")
        return numero
    except ValueError as mensaje:
        print(mensaje)
        print("Ingresaste un dato no valido")
        return False
    else:
        print("Numero ingresado exitoso")
    finally:
        print("PROGRAMA FINALIZADO")
        
print("Ingrese un numero")
numero=tomaNumero()
if numero is not False :
    print("El numero ingesado fue",numero)