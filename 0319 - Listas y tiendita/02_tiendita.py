# Lista de los productos
productos = ["papas", "refrescos", "tortillas", "jamon"]
# Lista de los precios
precio =    [12,      10.5,         20,         40]
# Lista del carrito con los productos
carrito_producto = []
# Lista de la cantidad en cada producto
carrito_cantidad = []

# Opción del menu
opcion = 0

# Mientras la opción  no sea igual a 6 repetir el menu
# Mientras la opción sea diferente a 6 repetir el menu
while opcion != 6:
    print("1. Mostrar productos")
    print("2. Mostrar el carrito")
    print("3. Agregar al carrito")
    print("4. Borrar un producto del carrito")
    print("5. Pagar productos")
    print("6. Salir")
    print("")
    opcion = int(input("Opción: "))
    print("")

    if opcion == 1:
        tamano = len(productos)
        print("No.    Nombre     Precio")
        for i in range(tamano):
            print(i+1,". ",productos[i],"  ", precio[i])

    elif opcion == 2:
        tamano = len(carrito_producto)
        print("----  Carrito ----------")
        print("No.    Nombre     Precio")
        for i in range(tamano):
            print(i+1,". ",carrito_producto[i],"  ", carrito_cantidad[i])

    elif opcion == 3:
        tamano = len(productos)
        print("No.    Nombre     Precio")
        for i in range(tamano):
            print(i+1,". ",productos[i],"  ", precio[i])
        print("------------------------")
        cual_producto = input("¿Cual producto quieres agregar?")

    elif opcion == 4:
        print("La opción es 4")
    elif opcion == 5:
        print("La opción es 5")
    elif opcion == 6:
        print("La opción es 6")
    else:
        print("La opción no existe.")








