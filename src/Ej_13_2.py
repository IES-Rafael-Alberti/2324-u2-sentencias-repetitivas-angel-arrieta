def resonar(grito):
    return grito


if __name__ == "__main__":
    eco = ""
    while eco != "salir":
        # Entrada y proceso
        eco = resonar(str(input("Cámara de eco\t")))
        if eco != "salir":
            # Salida
            print(eco)
        else:
            continue
