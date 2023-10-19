def recorre_inversa(palabra):
    resultado = ""
    for letra in palabra[::-1]:
        resultado += f"{letra}\n"
    return resultado[:-1]


if __name__ == "__main__":
    # Entrada, proceso y salida
    print(recorre_inversa(str(input("Dime una palabra\t"))))
