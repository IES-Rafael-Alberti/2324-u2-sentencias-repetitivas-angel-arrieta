def cuentaAtras(inicio):
    resultado = ""
    for n in range(inicio, -1, -1):
        resultado += f"{n}, "
    return resultado[:-2]


if __name__ == "__main__":
    # Entrada, proceso y salida
    print(cuentaAtras(int(input(">\t"))))
