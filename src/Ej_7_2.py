def tablaMultiplicar(numero):
    respuesta = ""
    for n in range(10):
        respuesta += f"{n+1} * {numero} = {(n+1)*numero}\n"
    return respuesta[:-1]


if __name__ == "__main__":
    print(tablaMultiplicar(int(input("Dime de que número quieres tu tabla de multiplicar:\t"))))
