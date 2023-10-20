def cuenta_digitos(linea: list):
    digitos = 0
    for titulo in linea:
        for numero in range(0, 10):
            digitos += titulo.count(str(numero))
    return digitos


def cuenta_lineas(libro: list):
    cantidad = 0
    for linea in libro:
        cantidad += 1
    return cantidad


if __name__ == "__main__":
    linea = []
    registro = []
    nuevo_titulo = ""
    # Proceso
    while nuevo_titulo != "*":
        nuevo_titulo = str(input("Dime títulos de libros"
        " (Introduce / para terminar la \nlinea"
        " ó * para terminar el programa)\n"))
        if nuevo_titulo == "/":
            registro.append(linea)
            digitos = cuenta_digitos(linea)
            print(f"Línea completa. Aparecen {digitos} dígitos numéricos.")
            linea = []
        elif nuevo_titulo == "*":
            cantidad_lineas = cuenta_lineas(registro)
        else:
            linea.append(nuevo_titulo)
    print(f"Fin. Se leyeron {cantidad_lineas} líneas completas.")
