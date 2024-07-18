def es_binario(var):
    for char in var:
        if char != '0' and char != '1':
            return False
    return True

cadena = input("Introduzca una cadena: ")
if es_binario(cadena):
    print(f"True")
else:
    print("False")
