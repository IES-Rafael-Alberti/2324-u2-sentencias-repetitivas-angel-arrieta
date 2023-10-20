def inversion(monto_inicial, interes, anos):
    cartilla = []
    resultado = ""
    for n in range(anos):
        monto_inicial *= 1 + interes / 100
        cartilla.append(round(monto_inicial, 2))
    for balance_final in cartilla:
        resultado += f"Año {cartilla.index(balance_final)+1} -- {balance_final}\n"
    return resultado[:-1]


if __name__ == "__main__":
    # Entrada
    balance_inicial = float(input("Calculadora de inversión\nBalance inicial:\t"))
    porcentaje = int(input("Porcentaje de interes:\t"))
    tiempo = int(input("Años de Inversión:\t"))
    # Proceso
    resultado_consulta = inversion(balance_inicial, porcentaje, tiempo)
    # Salida
    print(resultado_consulta)
