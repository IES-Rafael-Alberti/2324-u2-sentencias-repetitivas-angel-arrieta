def comparador(anterior, actual):
    if actual == 0:
        resultado = "fuera"
    elif actual > anterior:
        resultado = actual
    else:
        resultado = anterior
    return resultado


if __name__ == "__main__":
    mayor = 0
    nuevo = 0
    while nuevo != "fuera":
        # Entrada y proceso
        nuevo = comparador(mayor, int(input("Mete números para comparar\t")))
        if nuevo != "fuera":
            mayor = nuevo
    # Salida
    print(f"{mayor} es el número más grande de todos los  introducidos")
