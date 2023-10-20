def buscador_caracteres(frase, letra):
    resultado = ""
    if len(letra) != 1:
        resultado = "Solo una letra"
    else:
        encontrado = frase.find(letra)
        frase = frase[0:encontrado]
        if encontrado == 0:
            resultado = "Encontrado en posición 1"
        else:
            for posicion in range(len(frase)):
                if resultado == "":
                        resultado = "Posiciones donde no esta "
                resultado += f"{posicion+1}, "
            resultado = resultado[:-2] + f". Encontrado en posición {encontrado+1}."
    return resultado


if __name__ == "__main__":
    # Entrada
    oracion = str(input("Dime una frase\n"))
    caracter = str(input("Dime para buscar una letra\t"))
    # Proceso
    encontrado = buscador_caracteres(oracion, caracter)
    # Salida
    print(encontrado)
