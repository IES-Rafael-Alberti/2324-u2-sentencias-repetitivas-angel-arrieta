def unaVida(edad):
    resultado = ""
    for anos in range(edad):
         resultado += f"{anos + 1}\n"
    return resultado


if __name__ == "__main__":
    # Entrada
    edad = int(input("Introduzca su edad\t"))
    # Proceso
    recorrido_vida = unaVida(edad)
    # Salida
    print(recorrido_vida)
