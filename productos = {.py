productos = {
1: ( " Cafe " , 3000 , 20) ,
2: ( " Jugo natural " , 5000 , 15) ,
3: ( " Sandwich " , 8000 , 10) ,
4: ( " Empanada " , 2500 , 25) ,
5: ( " Hamburguesa " , 12000 , 8)
}


def registrar_productos(productos,pedido,codigo,cantidad):
    if codigo in productos:
        nombre, precio, stock = productos[codigo]
        if cantidad <= stock:
            pedido.append((nombre, precio, cantidad))
            productos[codigo] = (nombre, precio, stock - cantidad)
            print(f"Producto {nombre} agregado al pedido.")
        else:
            print(f"No hay suficiente stock de {nombre}. Stock disponible: {stock}.")
    else:
        print("Código de producto no válido.")

def calculat_totalPedido(pedido):
    total = 0
    for nombre,precio,cantidad in pedido:
        total += precio * cantidad
        return total


def mostrar_resumen(pedido):
    print("\nResumen del pedido:")
    for nombre, precio, cantidad in pedido:
        print(f"{nombre} - Precio: {precio} - Cantidad: {cantidad}")
    total = calculat_totalPedido(pedido)
    print(f"Total a pagar: {total}")
    if total >= 50000:
        print("¡Felicidades! has alcanzado el monto minimo para recibir descuento del 10% en tu compra")
        descuento = total * 0.10
    else:
        descuento = 0
    total_final = total - descuento

    print("----------------------------------------")
    print(f"Total: ${total:.0f}")
    print(f"Descuento: ${descuento:.0f}")
    print(f"TOTAL A PAGAR: ${total_final:.0f}")

def cafeteria():

    pedido = []
    opcion = 0

    while opcion != 3:

        print("\n========== CAFETERIA ==========")
        print("1. Mostrar productos")
        print("2. Agregar producto al pedido")
        print("3. Finalizar pedido")

        try:
            opcion = int(input("\nSeleccione una opcion: "))

            if opcion == 1:
                mostrar_productos(productos)

            elif opcion == 2:
                mostrar_productos(productos)

                codigo = int(input("\nIngrese el codigo del producto: "))
                cantidad = int(input("Ingrese la cantidad: "))

                registrar_producto(productos, pedido, codigo, cantidad)

            elif opcion == 3:
                if len(pedido) > 0:
                    mostrar_resumen(pedido)
                    print("\nGracias por comprar en nuestra cafeteria.")
                else:
                    print("\nNo se registraron productos en el pedido.")

            else:
                print("Opcion no valida.")

        except ValueError:
            print("Opcion no valida.")


# Ejecutar el programa
cafeteria()
