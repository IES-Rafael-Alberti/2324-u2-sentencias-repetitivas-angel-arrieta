def impares(ultimo):
    resultado = ""
    for n in range(0, ultimo, 2):
        resultado += f"{n+1}, "
    return resultado[:-2]


if __name__ == "__main__":
    # Entrada
    ultimo_numero = int(input("Lista de números impares. Dime hasta que número llego\t"))
    # Proceso
    lista_impares = impares(ultimo_numero)
    # Salida
    print(lista_impares)
