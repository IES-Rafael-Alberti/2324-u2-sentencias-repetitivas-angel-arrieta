def triangulo(niveles):
    dibujo = ""
    for columnas in range(niveles):
        for estrellas in range(columnas+1):
            dibujo += "*"
        dibujo += "\n"
    return dibujo[:-1]

if __name__ == "__main__":
    # Entrada, proceso y salida
    print(triangulo(int(input("Dime la altura del triángulo:\t"))))
