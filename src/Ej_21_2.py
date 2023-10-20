def compra(total_venta, ultimo_precio):
    if ultimo_precio < 0:
        resultado = total_venta
    else:
        resultado = total_venta + ultimo_precio
    return resultado


def descuento(pedido):
    if pedido >= 1000:
        resultado = pedido - (pedido/100*10)
    else:
        resultado = pedido
    return resultado


if __name__ == "__main__":
    total_compra = -1
    ultimo_monto = 1
    # Proceso
    while ultimo_monto != 0:
        total_compra = compra(total_compra, ultimo_monto)
        ultimo_monto = int(input("Ingresa los precios de los productos a comprar\n"
        "(Ingrese 0 para terminar)\t"))  # Entrada
        if ultimo_monto < 0:
            print("Ingrese otro monto")
    total_compra = descuento(total_compra)
    # Salida
    print(f"Total a pagar: {total_compra}")
