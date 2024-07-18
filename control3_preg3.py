def potencia(num, exp):
    if exp == 0:
        return 1
    else:
        return num * potencia(num, exp - 1)

numero = int(input("Introduce un número: "))
exponente = int(input("Introduce un exponente: "))
resultado = potencia(numero, exponente)
print(f"{numero} elevado a {exponente} es {resultado}")