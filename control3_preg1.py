def digitos(num):
    num_str = str(num)
    return len(num_str)

numero = int(input("Introduzca un número: "))
print(f"{numero} tiene {digitos(numero)} dígitos.")