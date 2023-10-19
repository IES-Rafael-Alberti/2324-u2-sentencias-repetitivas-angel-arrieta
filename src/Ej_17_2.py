def suma_digitos(numero):
    suma = 0
    numero = list(str(numero))
    for digito in numero:
        suma += int(digito)
    return suma


if __name__ == "__main__":
    # Entrada y proceso
    suma = suma_digitos(int(input("Dime un número para sumarle los digitos\t")))
    # Salida
    print(f"La suma de sus digitos es {suma}")
