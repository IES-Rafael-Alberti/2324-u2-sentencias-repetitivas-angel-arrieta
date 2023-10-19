def sumar_positivos(total, actual):
    if actual == 0:
        resultado = "fuera"
    elif actual < 0:
        resultado = total
    else:
        resultado = total + actual
    return resultado


if __name__ == "__main__":
    sumado = 0
    ultima_suma = 0
    while ultima_suma != "fuera":
        # Entrada y proceso
        ultima_suma = sumar_positivos(sumado, int(input("Mete números para sumar\t")))
        if ultima_suma != "fuera":
            sumado = ultima_suma
    # Salida
    print(f"{sumado} es la suma de todos los números positivos introducidos")
