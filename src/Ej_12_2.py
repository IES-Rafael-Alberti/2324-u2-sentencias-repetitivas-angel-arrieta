def recurrencia(frase, caracter):
    frecuencia = frase.count(caracter)
    return frecuencia


if __name__ == "__main__":
    # Entrada
    oracion = str(input("Dime una frase\n> "))
    letra = str(input("Dime una letra a buscar\t"))
    # Proceso
    veces = recurrencia(oracion.lower(), letra.lower())
    # Salida
    print(f"En {oracion} aparece {veces} {letra}")
