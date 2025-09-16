def suma(a, b):
    try:
        a, b = float(a), float(b)
        return a + b
    except ValueError:
        print("Error: Tipo de dato no válido.")
        return None


def resta(a, b):
    try:
        a, b = float(a), float(b)
        return a - b
    except ValueError:
        print("Error: Tipo de dato no válido.")
        return None


def producto(a, b):
    try:
        a, b = float(a), float(b)
        return a * b
    except ValueError:
        print("Error: Tipo de dato no válido.")
        return None


def division(a, b):
    try:
        a, b = float(a), float(b)
        if b == 0:
            raise ZeroDivisionError
        return a / b
    except ValueError:
        print("Error: Tipo de dato no válido.")
        return None
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero.")
        return None
