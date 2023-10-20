def contador_paridad(total_pares, total_impares, numero_nuevo):
    if numero_nuevo == -1:
        resultado = "fuera"
    elif numero_nuevo % 2 == 0:
        total_pares += 1
        resultado = total_pares, total_impares
    elif numero_nuevo % 2 == 1:
        total_impares += 1
        resultado = total_pares, total_impares
    return resultado


def suma_digitos(numero):
    resultado = 0
    numero = list(str(numero))
    if numero.count("-") > 0:
        numero.remove("-")
    for digito in numero:
        resultado += int(digito)
    return resultado


if __name__ == "__main__":
    numero_actual = 0
    pares = 0
    impares = 0
    while numero_actual != "terminar":
        numero_actual = int(input("Introduce numeros enteros\n(Introduce -1 para salir)\t"))
    #Proceso
        dupla_par_impar = contador_paridad(pares, impares, numero_actual)
        ultima_suma_digitos = suma_digitos(numero_actual)
        print(f"Suma de los digitos: {ultima_suma_digitos}")
        if dupla_par_impar == "fuera":
            numero_actual = "terminar"
        else:
            pares, impares = dupla_par_impar
    #Salida
    print(f"De todos los numeros introducidos {pares} son pares y {impares} son impares")
