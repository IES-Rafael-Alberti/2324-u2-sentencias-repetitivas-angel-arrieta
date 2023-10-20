def cuentaAtras(inicio):
    resultado = ""
    for n in range(inicio, -1, -1):
        resultado += f"{n}, "
    return resultado[:-2]


if __name__ == "__main__":
    # Entrada, proceso y salida
    primero = int(input("¿Desde que número comenzamos la cuenta atras?\t"))
    # Proceso
    cuenta_regresiva = cuentaAtras(primero)
    # Salida
    print(cuenta_regresiva)
