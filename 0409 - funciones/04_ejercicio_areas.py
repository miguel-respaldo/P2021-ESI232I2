# funcion menu sin parametros
def menu():
    print("1) Calcular el área de un rectángulo")
    print("2) Calcular el área de un triángulo")
    print("3) Calcular el área de un cuadrado")
    print("4) Calcular el área de un círculo")
    print("5) Salir")

opcion = 0
# Mientras la opcion sea deferente de 5
while opcion != 5:
    menu()
    opcion = int(input("Opción: "))
    if opcion == 1:
        print("opcion 1")
    elif opcion == 2:
        print("opcion 2")
    elif opcion == 3:
        print("opcion 3")
    elif opcion == 4:
        print("opcion 4")

