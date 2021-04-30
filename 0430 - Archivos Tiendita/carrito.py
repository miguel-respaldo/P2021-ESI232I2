import csv
import productos

# Nombre de los archivos para abrir
ARCHIVO_CARRITO="carrito.csv"

def inicializar():
    archivo = open(ARCHIVO_CARRITO,"w")
    archivo.write("Producto, Precio, Cantidad\n")
    archivo.close()


def mostrar():
    archivo = open(ARCHIVO_CARRITO,"r")
    lector = csv.reader(archivo)
    contador = 1
    print("----  Carrito ----------")
    print("{:<5s}{:<15s}{:>8s}{:>10s}".format("No.", "Nombre", "Precio", "Cantidad"))
    for fila in lector:
        if fila[0] == "Producto":
            continue
        print("{:<5d}{:<15s}{:>8.2f}{:>10d}".format(contador, fila[0], float(fila[1]), int(fila[2])))
        contador = contador + 1
    archivo.close()


def agregar (num_producto, cantidad):
    nombre_producto = productos.buscar_nombre(num_producto)
    precio_producto = productos.buscar_precio(num_producto)
    archivo = open(ARCHIVO_CARRITO,"a")
    archivo.write(nombre_producto + ", " + precio_producto + ", "+ str(cantidad) + "\n")
    archivo.close()

