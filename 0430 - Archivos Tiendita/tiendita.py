import productos
import carrito


def menu():
    print("")
    print("-------------------------------------")
    print("1. Mostrar productos")
    print("2. Mostrar el carrito")
    print("3. Agregar al carrito")
    print("4. Borrar un producto del carrito")
    print("5. Cantidad a pagar")
    print("6. Salir")
    print("")
    opcion = int(input("Opción: "))
    print("")
    return opcion


def agregar_al_carrito():
    productos.mostrar()
    print("------------------------")
    num_producto = int(input("Ingresa el número del prodcto a agregar: "))
    cant_producto = int(input("Cuantos articulos quieres de este producto: "))
    carrito.agregar(num_producto, cant_producto)


def tiendita():
    carrito.inicializar()
    opcion_menu = 0
    while opcion_menu != 6:
        opcion_menu = menu()
        if opcion_menu == 1:
            productos.mostrar()
        elif opcion_menu == 2:
            carrito.mostrar()
        elif opcion_menu == 3:
            agregar_al_carrito()


if __name__ == "__main__":
    tiendita()
