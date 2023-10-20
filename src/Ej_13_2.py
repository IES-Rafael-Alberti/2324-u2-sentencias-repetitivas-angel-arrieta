def resonar(grito):
    return grito


if __name__ == "__main__":
    eco = ""
    # Proceso
    while eco != "salir":
        eco = resonar(str(input("Cámara de eco\t"))) # Entrada
        if eco != "salir":
            # Salida
            print(eco)
