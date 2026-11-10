
# Parcial 3 - Logica de Programacion
# Integrantes: Jeremy Antoine Sotelo Scarpetta y Samuel Ayala Quinche

# 1. Diccionario de productos con tuplas
productos = {
    1: ("Cafe", 3000, 20),
    2: ("Jugo natural", 5000, 15),
    3: ("Sandwich", 8000, 10),
    4: ("Empanada", 2500, 25),
    5: ("Hamburguesa", 12000, 8)
}


# 2. Funcion para mostrar el catalogo
def mostrar_productos(productos):
    print("\n========== CATALOGO DE PRODUCTOS ==========")
    print("Codigo | Producto       | Precio | Existencias")
    print("--------------------------------------------")

    for codigo, datos in productos.items():
        nombre, precio, existencias = datos
        print(f"{codigo:<6} | {nombre:<14} | ${precio:<6} | {existencias}")


# 3. Funcion para registrar productos
def registrar_producto(productos, pedido, codigo, cantidad):

    if codigo not in productos:
        print("Producto no encontrado.")
        return

    if cantidad <= 0:
        print("Cantidad no valida.")
        return

    nombre, precio, existencias = productos[codigo]

    if cantidad > existencias:
        print("No hay suficientes unidades disponibles.")
        return

    subtotal = precio * cantidad

    # Guardar el producto como una tupla dentro de la lista
    pedido.append((codigo, nombre, cantidad, subtotal))

    # Actualizar las existencias del producto
    productos[codigo] = (nombre, precio, existencias - cantidad)

    print(f"{nombre} agregado correctamente al pedido.")


# 4. Funcion para calcular el total
def calcular_total(pedido):

    total = 0

    for producto in pedido:
        total += producto[3]

    return total


# 5. Funcion para mostrar el resumen del pedido
def mostrar_resumen(pedido):

    print("\n========== RESUMEN DEL PEDIDO ==========")
    print(f"{'Producto':<18} {'Cantidad':<12} {'Subtotal'}")
    print("----------------------------------------")

    for codigo, nombre, cantidad, subtotal in pedido:
        print(f"{nombre:<18} {cantidad:<12} ${subtotal}")

    total = calcular_total(pedido)

    # Aplicar descuento del 10% si cumple la condicion
    if total >= 50000:
        descuento = total * 0.10
    else:
        descuento = 0

    total_final = total - descuento

    print("----------------------------------------")
    print(f"Total: ${total:.0f}")
    print(f"Descuento: ${descuento:.0f}")
    print(f"TOTAL A PAGAR: ${total_final:.0f}")


# 6. Programa principal: menu de la cafeteria
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
        except ValueError:
            print("Opcion no valida.")
            continue

        if opcion == 1:

            mostrar_productos(productos)

        elif opcion == 2:

            mostrar_productos(productos)

            try:
                codigo = int(input("\nIngrese el codigo del producto: "))
                cantidad = int(input("Ingrese la cantidad: "))

                registrar_producto(productos, pedido, codigo, cantidad)

            except ValueError:
                print("Debe ingresar numeros enteros.")

        elif opcion == 3:

            if len(pedido) > 0:
                mostrar_resumen(pedido)
                print("\nGracias por comprar en nuestra cafeteria.")
            else:
                print("\nNo se registraron productos en el pedido.")

        else:

            print("Opcion no valida.")


# Ejecutar el programa
cafeteria()

