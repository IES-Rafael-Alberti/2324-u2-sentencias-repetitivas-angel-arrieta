def identificacion(usuario):
    if usuario == "contraseña":
        respuesta = "correcta"
    else:
        respuesta = "incorrecta"
    return respuesta


if __name__ == "__main__":
    # Entrada
    print("Introduzca la contraseña")
    # Proceso
    autentica = ""
    while autentica != "correcta":
        autentica = identificacion(str(input(">\t")))
        # Salida
        print(f"Contraseña {autentica}")

