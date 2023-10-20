def suma_digitos(numero):
    resultado = 0
    numero = list(str(numero))
    if numero.count("-") > 0:
        resultado = "No se sumar negativos"
    for digito in numero:
        resultado += int(digito)
    return resultado


if __name__ == "__main__":
    # Entrada
    numero = int(input("Dime un número entero positivo para sumarle los digitos\t"))
    # Proceso
    suma = suma_digitos(numero)
    # Salida
    if type(suma) != type(0):
        print(suma)
    else:
        print(f"La suma de sus digitos es {suma}")
